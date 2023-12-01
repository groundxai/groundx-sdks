/* tslint:disable */
/* eslint-disable */
/*
GroundX API

Ground Your RAG Apps in Fact not Fiction

The version of the OpenAPI document: 1.0.0
Contact: support@groundx.ai

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
import { BucketCreateRequest } from '../models';
// @ts-ignore
import { BucketListResponse } from '../models';
// @ts-ignore
import { BucketResponse } from '../models';
// @ts-ignore
import { BucketUpdateRequest } from '../models';
// @ts-ignore
import { BucketUpdateResponse } from '../models';
// @ts-ignore
import { MessageResponse } from '../models';
import { paginate } from "../pagination/paginate";
import type * as buffer from "buffer"
import { requestBeforeHook } from '../requestBeforeHook';
/**
 * BucketsApi - axios parameter creator
 * @export
 */
export const BucketsApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * create a new bucket.
         * @summary buckets.create
         * @param {BucketCreateRequest} bucketCreateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        create: async (bucketCreateRequest: BucketCreateRequest, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'bucketCreateRequest' is not null or undefined
            assertParamExists('create', 'bucketCreateRequest', bucketCreateRequest)
            const localVarPath = `/v1/bucket`;
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
            await setApiKeyToObject({ object: localVarHeaderParameter, keyParamName: "X-API-Key", configuration })

    
            localVarHeaderParameter['Content-Type'] = 'application/json';


            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            requestBeforeHook({
                requestBody: bucketCreateRequest,
                queryParameters: localVarQueryParameter,
                requestConfig: localVarRequestOptions,
                path: localVarPath,
                configuration
            });
            localVarRequestOptions.data = serializeDataIfNeeded(bucketCreateRequest, localVarRequestOptions, configuration)

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * delete a bucket.
         * @summary buckets.delete
         * @param {number} bucketId The bucketId of the bucket being deleted.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        delete: async (bucketId: number, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'bucketId' is not null or undefined
            assertParamExists('delete', 'bucketId', bucketId)
            const localVarPath = `/v1/bucket/{bucketId}`
                .replace(`{${"bucketId"}}`, encodeURIComponent(String(bucketId !== undefined ? bucketId : `-bucketId-`)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions: AxiosRequestConfig = { method: 'DELETE', ...baseOptions, ...options};
            const localVarHeaderParameter = configuration && !isBrowser() ? { "User-Agent": configuration.userAgent } : {} as any;
            const localVarQueryParameter = {} as any;

            // authentication ApiKeyAuth required
            await setApiKeyToObject({ object: localVarHeaderParameter, keyParamName: "X-API-Key", configuration })

    
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            requestBeforeHook({
                queryParameters: localVarQueryParameter,
                requestConfig: localVarRequestOptions,
                path: localVarPath,
                configuration
            });

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * look up a specific bucket by its bucketId.
         * @summary buckets.get
         * @param {number} bucketId The bucketId of the bucket to look up.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        get: async (bucketId: number, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'bucketId' is not null or undefined
            assertParamExists('get', 'bucketId', bucketId)
            const localVarPath = `/v1/bucket/{bucketId}`
                .replace(`{${"bucketId"}}`, encodeURIComponent(String(bucketId !== undefined ? bucketId : `-bucketId-`)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions: AxiosRequestConfig = { method: 'GET', ...baseOptions, ...options};
            const localVarHeaderParameter = configuration && !isBrowser() ? { "User-Agent": configuration.userAgent } : {} as any;
            const localVarQueryParameter = {} as any;

            // authentication ApiKeyAuth required
            await setApiKeyToObject({ object: localVarHeaderParameter, keyParamName: "X-API-Key", configuration })

    
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            requestBeforeHook({
                queryParameters: localVarQueryParameter,
                requestConfig: localVarRequestOptions,
                path: localVarPath,
                configuration
            });

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * List all buckets within your GroundX account
         * @summary buckets.list
         * @param {number} [n] The maximum number of returned documents. Accepts 1-100 with a default of 20.
         * @param {string} [nextToken] A token for pagination. If the number of documents for a given query is larger than n, the response will include a \&quot;nextToken\&quot; value. That token can be included in this field to retrieve the next batch of n documents.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        list: async (n?: number, nextToken?: string, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/v1/bucket`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions: AxiosRequestConfig = { method: 'GET', ...baseOptions, ...options};
            const localVarHeaderParameter = configuration && !isBrowser() ? { "User-Agent": configuration.userAgent } : {} as any;
            const localVarQueryParameter = {} as any;

            // authentication ApiKeyAuth required
            await setApiKeyToObject({ object: localVarHeaderParameter, keyParamName: "X-API-Key", configuration })
            if (n !== undefined) {
                localVarQueryParameter['n'] = n;
            }

            if (nextToken !== undefined) {
                localVarQueryParameter['nextToken'] = nextToken;
            }


    
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            requestBeforeHook({
                queryParameters: localVarQueryParameter,
                requestConfig: localVarRequestOptions,
                path: localVarPath,
                configuration
            });

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * Rename a bucket
         * @summary buckets.update
         * @param {number} bucketId The bucketId of the bucket being updated.
         * @param {BucketUpdateRequest} bucketUpdateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        update: async (bucketId: number, bucketUpdateRequest: BucketUpdateRequest, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'bucketId' is not null or undefined
            assertParamExists('update', 'bucketId', bucketId)
            // verify required parameter 'bucketUpdateRequest' is not null or undefined
            assertParamExists('update', 'bucketUpdateRequest', bucketUpdateRequest)
            const localVarPath = `/v1/bucket/{bucketId}`
                .replace(`{${"bucketId"}}`, encodeURIComponent(String(bucketId !== undefined ? bucketId : `-bucketId-`)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions: AxiosRequestConfig = { method: 'PUT', ...baseOptions, ...options};
            const localVarHeaderParameter = configuration && !isBrowser() ? { "User-Agent": configuration.userAgent } : {} as any;
            const localVarQueryParameter = {} as any;

            // authentication ApiKeyAuth required
            await setApiKeyToObject({ object: localVarHeaderParameter, keyParamName: "X-API-Key", configuration })

    
            localVarHeaderParameter['Content-Type'] = 'application/json';


            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            requestBeforeHook({
                requestBody: bucketUpdateRequest,
                queryParameters: localVarQueryParameter,
                requestConfig: localVarRequestOptions,
                path: localVarPath,
                configuration
            });
            localVarRequestOptions.data = serializeDataIfNeeded(bucketUpdateRequest, localVarRequestOptions, configuration)

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * BucketsApi - functional programming interface
 * @export
 */
export const BucketsApiFp = function(configuration?: Configuration) {
    const localVarAxiosParamCreator = BucketsApiAxiosParamCreator(configuration)
    return {
        /**
         * create a new bucket.
         * @summary buckets.create
         * @param {BucketsApiCreateRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async create(requestParameters: BucketsApiCreateRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<BucketResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.create(requestParameters, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * delete a bucket.
         * @summary buckets.delete
         * @param {BucketsApiDeleteRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async delete(requestParameters: BucketsApiDeleteRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<MessageResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.delete(requestParameters.bucketId, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * look up a specific bucket by its bucketId.
         * @summary buckets.get
         * @param {BucketsApiGetRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async get(requestParameters: BucketsApiGetRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<BucketResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.get(requestParameters.bucketId, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * List all buckets within your GroundX account
         * @summary buckets.list
         * @param {BucketsApiListRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async list(requestParameters: BucketsApiListRequest = {}, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<BucketListResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.list(requestParameters.n, requestParameters.nextToken, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * Rename a bucket
         * @summary buckets.update
         * @param {BucketsApiUpdateRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async update(requestParameters: BucketsApiUpdateRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<BucketUpdateResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.update(requestParameters.bucketId, requestParameters, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
    }
};

/**
 * BucketsApi - factory interface
 * @export
 */
export const BucketsApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = BucketsApiFp(configuration)
    return {
        /**
         * create a new bucket.
         * @summary buckets.create
         * @param {BucketsApiCreateRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        create(requestParameters: BucketsApiCreateRequest, options?: AxiosRequestConfig): AxiosPromise<BucketResponse> {
            return localVarFp.create(requestParameters, options).then((request) => request(axios, basePath));
        },
        /**
         * delete a bucket.
         * @summary buckets.delete
         * @param {BucketsApiDeleteRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        delete(requestParameters: BucketsApiDeleteRequest, options?: AxiosRequestConfig): AxiosPromise<MessageResponse> {
            return localVarFp.delete(requestParameters, options).then((request) => request(axios, basePath));
        },
        /**
         * look up a specific bucket by its bucketId.
         * @summary buckets.get
         * @param {BucketsApiGetRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        get(requestParameters: BucketsApiGetRequest, options?: AxiosRequestConfig): AxiosPromise<BucketResponse> {
            return localVarFp.get(requestParameters, options).then((request) => request(axios, basePath));
        },
        /**
         * List all buckets within your GroundX account
         * @summary buckets.list
         * @param {BucketsApiListRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        list(requestParameters: BucketsApiListRequest = {}, options?: AxiosRequestConfig): AxiosPromise<BucketListResponse> {
            return localVarFp.list(requestParameters, options).then((request) => request(axios, basePath));
        },
        /**
         * Rename a bucket
         * @summary buckets.update
         * @param {BucketsApiUpdateRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        update(requestParameters: BucketsApiUpdateRequest, options?: AxiosRequestConfig): AxiosPromise<BucketUpdateResponse> {
            return localVarFp.update(requestParameters, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for create operation in BucketsApi.
 * @export
 * @interface BucketsApiCreateRequest
 */
export type BucketsApiCreateRequest = {
    
} & BucketCreateRequest

/**
 * Request parameters for delete operation in BucketsApi.
 * @export
 * @interface BucketsApiDeleteRequest
 */
export type BucketsApiDeleteRequest = {
    
    /**
    * The bucketId of the bucket being deleted.
    * @type {number}
    * @memberof BucketsApiDelete
    */
    readonly bucketId: number
    
}

/**
 * Request parameters for get operation in BucketsApi.
 * @export
 * @interface BucketsApiGetRequest
 */
export type BucketsApiGetRequest = {
    
    /**
    * The bucketId of the bucket to look up.
    * @type {number}
    * @memberof BucketsApiGet
    */
    readonly bucketId: number
    
}

/**
 * Request parameters for list operation in BucketsApi.
 * @export
 * @interface BucketsApiListRequest
 */
export type BucketsApiListRequest = {
    
    /**
    * The maximum number of returned documents. Accepts 1-100 with a default of 20.
    * @type {number}
    * @memberof BucketsApiList
    */
    readonly n?: number
    
    /**
    * A token for pagination. If the number of documents for a given query is larger than n, the response will include a \"nextToken\" value. That token can be included in this field to retrieve the next batch of n documents.
    * @type {string}
    * @memberof BucketsApiList
    */
    readonly nextToken?: string
    
}

/**
 * Request parameters for update operation in BucketsApi.
 * @export
 * @interface BucketsApiUpdateRequest
 */
export type BucketsApiUpdateRequest = {
    
    /**
    * The bucketId of the bucket being updated.
    * @type {number}
    * @memberof BucketsApiUpdate
    */
    readonly bucketId: number
    
} & BucketUpdateRequest

/**
 * BucketsApiGenerated - object-oriented interface
 * @export
 * @class BucketsApiGenerated
 * @extends {BaseAPI}
 */
export class BucketsApiGenerated extends BaseAPI {
    /**
     * create a new bucket.
     * @summary buckets.create
     * @param {BucketsApiCreateRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof BucketsApiGenerated
     */
    public create(requestParameters: BucketsApiCreateRequest, options?: AxiosRequestConfig) {
        return BucketsApiFp(this.configuration).create(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * delete a bucket.
     * @summary buckets.delete
     * @param {BucketsApiDeleteRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof BucketsApiGenerated
     */
    public delete(requestParameters: BucketsApiDeleteRequest, options?: AxiosRequestConfig) {
        return BucketsApiFp(this.configuration).delete(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * look up a specific bucket by its bucketId.
     * @summary buckets.get
     * @param {BucketsApiGetRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof BucketsApiGenerated
     */
    public get(requestParameters: BucketsApiGetRequest, options?: AxiosRequestConfig) {
        return BucketsApiFp(this.configuration).get(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * List all buckets within your GroundX account
     * @summary buckets.list
     * @param {BucketsApiListRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof BucketsApiGenerated
     */
    public list(requestParameters: BucketsApiListRequest = {}, options?: AxiosRequestConfig) {
        return BucketsApiFp(this.configuration).list(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * Rename a bucket
     * @summary buckets.update
     * @param {BucketsApiUpdateRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof BucketsApiGenerated
     */
    public update(requestParameters: BucketsApiUpdateRequest, options?: AxiosRequestConfig) {
        return BucketsApiFp(this.configuration).update(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }
}
