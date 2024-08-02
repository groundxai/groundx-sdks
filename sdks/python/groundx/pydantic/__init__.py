from importlib import metadata


try:
    from pydantic.v1 import *
except ImportError:
    from pydantic import *


try:
    _PYDANTIC_MAJOR_VERSION: int = int(metadata.version("pydantic").split(".")[0])
except metadata.PackageNotFoundError:
    _PYDANTIC_MAJOR_VERSION = 0
