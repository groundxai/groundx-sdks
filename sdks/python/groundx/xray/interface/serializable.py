# coding: utf-8

"""
Abstraction of langchain serializable methods and classes
"""

from abc import ABC
from typing import (
    Any,
    Dict,
    List,
    Literal,
    Optional,
    TypedDict,
    Union,
    cast,
)

from typing_extensions import NotRequired

from groundx.pydantic import BaseModel


class BaseSerialized(TypedDict):
    lc: int
    id: List[str]
    name: NotRequired[str]
    graph: NotRequired[Dict[str, Any]]


class SerializedConstructor(BaseSerialized):
    type: Literal["constructor"]
    kwargs: Dict[str, Any]


class SerializedSecret(BaseSerialized):
    type: Literal["secret"]


class SerializedNotImplemented(BaseSerialized):
    type: Literal["not_implemented"]
    repr: Optional[str]


def try_neq_default(value: Any, key: str, model: BaseModel) -> bool:
    try:
        return model.__fields__[key].get_default() != value
    except Exception:
        return True


class Serializable(BaseModel, ABC):
    @classmethod
    def is_lc_serializable(cls) -> bool:
        return False

    @classmethod
    def get_lc_namespace(cls) -> List[str]:
        return cls.__module__.split(".")

    @property
    def lc_secrets(self) -> Dict[str, str]:

        return dict()

    @property
    def lc_attributes(self) -> Dict:
        return {}

    @classmethod
    def lc_id(cls) -> List[str]:
        return [*cls.get_lc_namespace(), cls.__name__]

    class Config:
        extra = "ignore"

    def __repr_args__(self) -> Any:
        return [
            (k, v)
            for k, v in super().__repr_args__()
            if (k not in self.__fields__ or try_neq_default(v, k, self))
        ]

    def to_json(self) -> Union[SerializedConstructor, SerializedNotImplemented]:
        if not self.is_lc_serializable():
            return self.to_json_not_implemented()

        secrets = dict()
        # Get latest values for kwargs if there is an attribute with same name
        lc_kwargs = {
            k: getattr(self, k, v)
            for k, v in self
            if not (self.__exclude_fields__ or {}).get(k, False)  # type: ignore
            and _is_field_useful(self, k, v)
        }

        # Merge the lc_secrets and lc_attributes from every class in the MRO
        for cls in [None, *self.__class__.mro()]:
            # Once we get to Serializable, we're done
            if cls is Serializable:
                break

            if cls:
                deprecated_attributes = [
                    "lc_namespace",
                    "lc_serializable",
                ]

                for attr in deprecated_attributes:
                    if hasattr(cls, attr):
                        raise ValueError(
                            f"Class {self.__class__} has a deprecated "
                            f"attribute {attr}. Please use the corresponding "
                            f"classmethod instead."
                        )

            # Get a reference to self bound to each class in the MRO
            this = cast(Serializable, self if cls is None else super(cls, self))

            secrets.update(this.lc_secrets)
            # Now also add the aliases for the secrets
            # This ensures known secret aliases are hidden.
            # Note: this does NOT hide any other extra kwargs
            # that are not present in the fields.
            for key in list(secrets):
                value = secrets[key]
                if key in this.__fields__:
                    secrets[this.__fields__[key].alias] = value
            lc_kwargs.update(this.lc_attributes)

        # include all secrets, even if not specified in kwargs
        # as these secrets may be passed as an environment variable instead
        for key in secrets.keys():
            secret_value = getattr(self, key, None) or lc_kwargs.get(key)
            if secret_value is not None:
                lc_kwargs.update({key: secret_value})

        return {
            "lc": 1,
            "type": "constructor",
            "id": self.lc_id(),
            "kwargs": (
                lc_kwargs if not secrets else _replace_secrets(lc_kwargs, secrets)
            ),
        }

    def to_json_not_implemented(self) -> SerializedNotImplemented:
        return to_json_not_implemented(self)


def _is_field_useful(inst: Serializable, key: str, value: Any) -> bool:
    field = inst.__fields__.get(key)
    if not field:
        return False
    return field.required is True or value or field.get_default() != value


def _replace_secrets(
    root: Dict[Any, Any], secrets_map: Dict[str, str]
) -> Dict[Any, Any]:
    result = root.copy()
    for path, secret_id in secrets_map.items():
        [*parts, last] = path.split(".")
        current = result
        for part in parts:
            if part not in current:
                break
            current[part] = current[part].copy()
            current = current[part]
        if last in current:
            current[last] = {
                "lc": 1,
                "type": "secret",
                "id": [secret_id],
            }
    return result


def _is_field_useful(inst: Serializable, key: str, value: Any) -> bool:
    field = inst.__fields__.get(key)
    if not field:
        return False
    return field.required is True or value or field.get_default() != value


def _replace_secrets(
    root: Dict[Any, Any], secrets_map: Dict[str, str]
) -> Dict[Any, Any]:
    result = root.copy()
    for path, secret_id in secrets_map.items():
        [*parts, last] = path.split(".")
        current = result
        for part in parts:
            if part not in current:
                break
            current[part] = current[part].copy()
            current = current[part]
        if last in current:
            current[last] = {
                "lc": 1,
                "type": "secret",
                "id": [secret_id],
            }
    return result


def to_json_not_implemented(obj: object) -> SerializedNotImplemented:
    _id: List[str] = []
    try:
        if hasattr(obj, "__name__"):
            _id = [*obj.__module__.split("."), obj.__name__]
        elif hasattr(obj, "__class__"):
            _id = [*obj.__class__.__module__.split("."), obj.__class__.__name__]
    except Exception:
        pass

    result: SerializedNotImplemented = {
        "lc": 1,
        "type": "not_implemented",
        "id": _id,
        "repr": None,
    }
    try:
        result["repr"] = repr(obj)
    except Exception:
        pass
    return result
