/* tslint:disable */
/* eslint-disable */
/*
GroundX APIs

RAG Made Simple, Secure and Hallucination Free

The version of the OpenAPI document: 1.3.26
Contact: support@eyelevel.ai

NOTE: This file is auto generated by Konfig (https://konfigthis.com).
*/

import globalAxios, { AxiosPromise, AxiosInstance, AxiosRequestConfig } from 'axios';
import { Configuration } from '../configuration';
// Some imports not used depending on template conditions
// @ts-ignore
import { DUMMY_BASE_URL, assertParamExists, setApiKeyToObject, setBasicAuthToObject, setBearerAuthToObject, setSearchParams, serializeDataIfNeeded, toPathString, createRequestFunction, isBrowser } from '../common';
import { fromBuffer } from "file-type/browser"
const FormData = require("form-data")
// @ts-ignore
import { BASE_PATH, COLLECTION_FORMATS, RequestArgs, BaseAPI, RequiredError } from '../base';
// @ts-ignore
import { SearchContentIdParameter } from '../models';
// @ts-ignore
import { SearchDocumentsRequest } from '../models';
// @ts-ignore
import { SearchRequest } from '../models';
// @ts-ignore
import { SearchResponse } from '../models';
import { paginate } from "../pagination/paginate";
import type * as buffer from "buffer"
import { requestBeforeHook } from '../requestBeforeHook';
/**
 * SearchApi - axios parameter creator
 * @export
 */
export const SearchApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * Search documents on GroundX for the most relevant information to a given query.  The result of this query is typically used in one of two ways; result[\'search\'][\'text\'] can be used to provide context to a language model, facilitating RAG, or result[\'search\'][\'results\'] can be used to observe chunks of text which are relevant to the query, facilitating citation.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 
         * @summary search.content
         * @param {SearchContentIdParameter} id The bucketId, groupId, projectId, or documentId to be searched. The document or documents within the specified container will be compared to the query, and relevant information will be extracted.
         * @param {number} [n] The maximum number of returned search results. Accepts 1-100 with a default of 20.
         * @param {string} [nextToken] A token for pagination. If the number of search results for a given query is larger than n, the response will include a \&quot;nextToken\&quot; value. That token can be included in this field to retrieve the next batch of n search results.
         * @param {number} [verbosity] The amount of data returned with each search result. 0 &#x3D;&#x3D; no search results, only the recommended context. 1 &#x3D;&#x3D; search results but no searchData. 2 &#x3D;&#x3D; search results and searchData.
         * @param {SearchRequest} [searchRequest] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        content: async (id: SearchContentIdParameter, n?: number, nextToken?: string, verbosity?: number, searchRequest?: SearchRequest, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('content', 'id', id)
            const localVarPath = `/v1/search/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id !== undefined ? id : `-id-`)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions: AxiosRequestConfig = { method: 'POST', ...baseOptions, ...options};
            const localVarHeaderParameter = configuration && !isBrowser() ? { "User-Agent": configuration.userAgent } : {} as any;
            const localVarQueryParameter = {} as any;

            // authentication ApiKeyAuth required
            await setApiKeyToObject({ object: localVarHeaderParameter, key: "X-API-Key", keyParamName: "xAPIKey", configuration })
            if (n !== undefined) {
                localVarQueryParameter['n'] = n;
            }

            if (nextToken !== undefined) {
                localVarQueryParameter['nextToken'] = nextToken;
            }

            if (verbosity !== undefined) {
                localVarQueryParameter['verbosity'] = verbosity;
            }


    
            localVarHeaderParameter['Content-Type'] = 'application/json';


            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            requestBeforeHook({
                requestBody: searchRequest,
                queryParameters: localVarQueryParameter,
                requestConfig: localVarRequestOptions,
                path: localVarPath,
                configuration,
                pathTemplate: '/v1/search/{id}',
                httpMethod: 'POST'
            });
            localVarRequestOptions.data = serializeDataIfNeeded(searchRequest, localVarRequestOptions, configuration)

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * Search documents on GroundX for the most relevant information to a given query by documentId(s).  The result of this query is typically used in one of two ways; result[\'search\'][\'text\'] can be used to provide context to a language model, facilitating RAG, or result[\'search\'][\'results\'] can be used to observe chunks of text which are relevant to the query, facilitating citation.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 
         * @summary search.documents
         * @param {number} [n] The maximum number of returned search results. Accepts 1-100 with a default of 20.
         * @param {string} [nextToken] A token for pagination. If the number of search results for a given query is larger than n, the response will include a \&quot;nextToken\&quot; value. That token can be included in this field to retrieve the next batch of n search results.
         * @param {number} [verbosity] The amount of data returned with each search result. 0 &#x3D;&#x3D; no search results, only the recommended context. 1 &#x3D;&#x3D; search results but no searchData. 2 &#x3D;&#x3D; search results and searchData.
         * @param {SearchDocumentsRequest} [searchDocumentsRequest] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        documents: async (n?: number, nextToken?: string, verbosity?: number, searchDocumentsRequest?: SearchDocumentsRequest, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/v1/search/documents`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions: AxiosRequestConfig = { method: 'POST', ...baseOptions, ...options};
            const localVarHeaderParameter = configuration && !isBrowser() ? { "User-Agent": configuration.userAgent } : {} as any;
            const localVarQueryParameter = {} as any;

            // authentication ApiKeyAuth required
            await setApiKeyToObject({ object: localVarHeaderParameter, key: "X-API-Key", keyParamName: "xAPIKey", configuration })
            if (n !== undefined) {
                localVarQueryParameter['n'] = n;
            }

            if (nextToken !== undefined) {
                localVarQueryParameter['nextToken'] = nextToken;
            }

            if (verbosity !== undefined) {
                localVarQueryParameter['verbosity'] = verbosity;
            }


    
            localVarHeaderParameter['Content-Type'] = 'application/json';


            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            requestBeforeHook({
                requestBody: searchDocumentsRequest,
                queryParameters: localVarQueryParameter,
                requestConfig: localVarRequestOptions,
                path: localVarPath,
                configuration,
                pathTemplate: '/v1/search/documents',
                httpMethod: 'POST'
            });
            localVarRequestOptions.data = serializeDataIfNeeded(searchDocumentsRequest, localVarRequestOptions, configuration)

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * SearchApi - functional programming interface
 * @export
 */
export const SearchApiFp = function(configuration?: Configuration) {
    const localVarAxiosParamCreator = SearchApiAxiosParamCreator(configuration)
    return {
        /**
         * Search documents on GroundX for the most relevant information to a given query.  The result of this query is typically used in one of two ways; result[\'search\'][\'text\'] can be used to provide context to a language model, facilitating RAG, or result[\'search\'][\'results\'] can be used to observe chunks of text which are relevant to the query, facilitating citation.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 
         * @summary search.content
         * @param {SearchApiContentRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async content(requestParameters: SearchApiContentRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<SearchResponse>> {
            const searchRequest: SearchRequest = {
                query: requestParameters.query,
                relevance: requestParameters.relevance
            };
            const localVarAxiosArgs = await localVarAxiosParamCreator.content(requestParameters.id, requestParameters.n, requestParameters.nextToken, requestParameters.verbosity, searchRequest, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * Search documents on GroundX for the most relevant information to a given query by documentId(s).  The result of this query is typically used in one of two ways; result[\'search\'][\'text\'] can be used to provide context to a language model, facilitating RAG, or result[\'search\'][\'results\'] can be used to observe chunks of text which are relevant to the query, facilitating citation.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 
         * @summary search.documents
         * @param {SearchApiDocumentsRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async documents(requestParameters: SearchApiDocumentsRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<SearchResponse>> {
            const searchDocumentsRequest: SearchDocumentsRequest = {
                query: requestParameters.query,
                documentIds: requestParameters.documentIds,
                relevance: requestParameters.relevance
            };
            const localVarAxiosArgs = await localVarAxiosParamCreator.documents(requestParameters.n, requestParameters.nextToken, requestParameters.verbosity, searchDocumentsRequest, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
    }
};

/**
 * SearchApi - factory interface
 * @export
 */
export const SearchApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = SearchApiFp(configuration)
    return {
        /**
         * Search documents on GroundX for the most relevant information to a given query.  The result of this query is typically used in one of two ways; result[\'search\'][\'text\'] can be used to provide context to a language model, facilitating RAG, or result[\'search\'][\'results\'] can be used to observe chunks of text which are relevant to the query, facilitating citation.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 
         * @summary search.content
         * @param {SearchApiContentRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        content(requestParameters: SearchApiContentRequest, options?: AxiosRequestConfig): AxiosPromise<SearchResponse> {
            return localVarFp.content(requestParameters, options).then((request) => request(axios, basePath));
        },
        /**
         * Search documents on GroundX for the most relevant information to a given query by documentId(s).  The result of this query is typically used in one of two ways; result[\'search\'][\'text\'] can be used to provide context to a language model, facilitating RAG, or result[\'search\'][\'results\'] can be used to observe chunks of text which are relevant to the query, facilitating citation.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 
         * @summary search.documents
         * @param {SearchApiDocumentsRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        documents(requestParameters: SearchApiDocumentsRequest, options?: AxiosRequestConfig): AxiosPromise<SearchResponse> {
            return localVarFp.documents(requestParameters, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for content operation in SearchApi.
 * @export
 * @interface SearchApiContentRequest
 */
export type SearchApiContentRequest = {
    
    /**
    * The bucketId, groupId, projectId, or documentId to be searched. The document or documents within the specified container will be compared to the query, and relevant information will be extracted.
    * @type {SearchContentIdParameter}
    * @memberof SearchApiContent
    */
    readonly id: SearchContentIdParameter
    
    /**
    * The maximum number of returned search results. Accepts 1-100 with a default of 20.
    * @type {number}
    * @memberof SearchApiContent
    */
    readonly n?: number
    
    /**
    * A token for pagination. If the number of search results for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n search results.
    * @type {string}
    * @memberof SearchApiContent
    */
    readonly nextToken?: string
    
    /**
    * The amount of data returned with each search result. 0 == no search results, only the recommended context. 1 == search results but no searchData. 2 == search results and searchData.
    * @type {number}
    * @memberof SearchApiContent
    */
    readonly verbosity?: number
    
} & SearchRequest

/**
 * Request parameters for documents operation in SearchApi.
 * @export
 * @interface SearchApiDocumentsRequest
 */
export type SearchApiDocumentsRequest = {
    
    /**
    * The maximum number of returned search results. Accepts 1-100 with a default of 20.
    * @type {number}
    * @memberof SearchApiDocuments
    */
    readonly n?: number
    
    /**
    * A token for pagination. If the number of search results for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n search results.
    * @type {string}
    * @memberof SearchApiDocuments
    */
    readonly nextToken?: string
    
    /**
    * The amount of data returned with each search result. 0 == no search results, only the recommended context. 1 == search results but no searchData. 2 == search results and searchData.
    * @type {number}
    * @memberof SearchApiDocuments
    */
    readonly verbosity?: number
    
} & SearchDocumentsRequest

/**
 * SearchApiGenerated - object-oriented interface
 * @export
 * @class SearchApiGenerated
 * @extends {BaseAPI}
 */
export class SearchApiGenerated extends BaseAPI {
    /**
     * Search documents on GroundX for the most relevant information to a given query.  The result of this query is typically used in one of two ways; result[\'search\'][\'text\'] can be used to provide context to a language model, facilitating RAG, or result[\'search\'][\'results\'] can be used to observe chunks of text which are relevant to the query, facilitating citation.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 
     * @summary search.content
     * @param {SearchApiContentRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof SearchApiGenerated
     */
    public content(requestParameters: SearchApiContentRequest, options?: AxiosRequestConfig) {
        return SearchApiFp(this.configuration).content(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * Search documents on GroundX for the most relevant information to a given query by documentId(s).  The result of this query is typically used in one of two ways; result[\'search\'][\'text\'] can be used to provide context to a language model, facilitating RAG, or result[\'search\'][\'results\'] can be used to observe chunks of text which are relevant to the query, facilitating citation.  Interact with the \"Request Body\" below to explore the arguments of this function. Enter your GroundX API key to send a request directly from this web page. Select your language of choice to structure a code snippet based on your specified arguments. 
     * @summary search.documents
     * @param {SearchApiDocumentsRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof SearchApiGenerated
     */
    public documents(requestParameters: SearchApiDocumentsRequest, options?: AxiosRequestConfig) {
        return SearchApiFp(this.configuration).documents(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }
}
