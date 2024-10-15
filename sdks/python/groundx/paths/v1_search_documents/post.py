# coding: utf-8

"""
    GroundX APIs

    RAG Made Simple, Secure and Hallucination Free

    The version of the OpenAPI document: 1.3.26
    Contact: support@eyelevel.ai
    Created by: https://www.eyelevel.ai/
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from groundx.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from groundx.api_response import AsyncGeneratorResponse
from groundx import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from groundx import schemas  # noqa: F401

from groundx.model.search_documents_request import SearchDocumentsRequest as SearchDocumentsRequestSchema
from groundx.model.search_documents_request_document_ids import SearchDocumentsRequestDocumentIds as SearchDocumentsRequestDocumentIdsSchema
from groundx.model.search_response import SearchResponse as SearchResponseSchema

from groundx.type.search_documents_request_document_ids import SearchDocumentsRequestDocumentIds
from groundx.type.search_response import SearchResponse
from groundx.type.search_documents_request import SearchDocumentsRequest

from . import path

# Query params


class NSchema(
    schemas.IntSchema
):


    class MetaOapg:
        inclusive_maximum = 100
        inclusive_minimum = 1
NextTokenSchema = schemas.StrSchema


class VerbositySchema(
    schemas.IntSchema
):


    class MetaOapg:
        inclusive_maximum = 2
        inclusive_minimum = 0
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'n': typing.Union[NSchema, decimal.Decimal, int, ],
        'nextToken': typing.Union[NextTokenSchema, str, ],
        'verbosity': typing.Union[VerbositySchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_n = api_client.QueryParameter(
    name="n",
    style=api_client.ParameterStyle.FORM,
    schema=NSchema,
    explode=True,
)
request_query_next_token = api_client.QueryParameter(
    name="nextToken",
    style=api_client.ParameterStyle.FORM,
    schema=NextTokenSchema,
    explode=True,
)
request_query_verbosity = api_client.QueryParameter(
    name="verbosity",
    style=api_client.ParameterStyle.FORM,
    schema=VerbositySchema,
    explode=True,
)
# body param
SchemaForRequestBodyApplicationJson = SearchDocumentsRequestSchema


request_body_search_documents_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'ApiKeyAuth',
]
SchemaFor200ResponseBodyApplicationJson = SearchResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: SearchResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: SearchResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _documents_mapped_args(
        self,
        query: str,
        document_ids: SearchDocumentsRequestDocumentIds,
        relevance: typing.Optional[typing.Union[int, float]] = None,
        n: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        verbosity: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        if query is not None:
            _body["query"] = query
        if document_ids is not None:
            _body["documentIds"] = document_ids
        if relevance is not None:
            _body["relevance"] = relevance
        args.body = _body
        if n is not None:
            _query_params["n"] = n
        if next_token is not None:
            _query_params["nextToken"] = next_token
        if verbosity is not None:
            _query_params["verbosity"] = verbosity
        args.query = _query_params
        return args

    async def _adocuments_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        search.documents
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_n,
            request_query_next_token,
            request_query_verbosity,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/search/documents',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_search_documents_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _documents_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        search.documents
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_n,
            request_query_next_token,
            request_query_verbosity,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/search/documents',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_search_documents_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class Documents(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def adocuments(
        self,
        query: str,
        document_ids: SearchDocumentsRequestDocumentIds,
        relevance: typing.Optional[typing.Union[int, float]] = None,
        n: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        verbosity: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._documents_mapped_args(
            query=query,
            document_ids=document_ids,
            relevance=relevance,
            n=n,
            next_token=next_token,
            verbosity=verbosity,
        )
        return await self._adocuments_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def documents(
        self,
        query: str,
        document_ids: SearchDocumentsRequestDocumentIds,
        relevance: typing.Optional[typing.Union[int, float]] = None,
        n: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        verbosity: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """ Search documents on GroundX for the most relevant information to a given query by documentId(s).  The result of this query is typically used in one of two ways; result['search']['text'] can be used to provide context to a language model, facilitating RAG, or result['search']['results'] can be used to observe chunks of text which are relevant to the query, facilitating citation.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.  """
        args = self._documents_mapped_args(
            query=query,
            document_ids=document_ids,
            relevance=relevance,
            n=n,
            next_token=next_token,
            verbosity=verbosity,
        )
        return self._documents_oapg(
            body=args.body,
            query_params=args.query,
        )

class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        query: str,
        document_ids: SearchDocumentsRequestDocumentIds,
        relevance: typing.Optional[typing.Union[int, float]] = None,
        n: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        verbosity: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._documents_mapped_args(
            query=query,
            document_ids=document_ids,
            relevance=relevance,
            n=n,
            next_token=next_token,
            verbosity=verbosity,
        )
        return await self._adocuments_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        query: str,
        document_ids: SearchDocumentsRequestDocumentIds,
        relevance: typing.Optional[typing.Union[int, float]] = None,
        n: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        verbosity: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """ Search documents on GroundX for the most relevant information to a given query by documentId(s).  The result of this query is typically used in one of two ways; result['search']['text'] can be used to provide context to a language model, facilitating RAG, or result['search']['results'] can be used to observe chunks of text which are relevant to the query, facilitating citation.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments.  """
        args = self._documents_mapped_args(
            query=query,
            document_ids=document_ids,
            relevance=relevance,
            n=n,
            next_token=next_token,
            verbosity=verbosity,
        )
        return self._documents_oapg(
            body=args.body,
            query_params=args.query,
        )

