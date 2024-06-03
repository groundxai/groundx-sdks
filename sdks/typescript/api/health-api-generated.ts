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
import { HealthResponse } from '../models';
import { paginate } from "../pagination/paginate";
import type * as buffer from "buffer"
import { requestBeforeHook } from '../requestBeforeHook';
/**
 * HealthApi - axios parameter creator
 * @export
 */
export const HealthApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * Look up the current health status of a specific service. Statuses update every 5 minutes. 
         * @summary get
         * @param {string} service The name of the service to look up.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        get: async (service: string, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'service' is not null or undefined
            assertParamExists('get', 'service', service)
            const localVarPath = `/v1/health/{service}`
                .replace(`{${"service"}}`, encodeURIComponent(String(service !== undefined ? service : `-service-`)));
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
            await setApiKeyToObject({ object: localVarHeaderParameter, key: "X-API-Key", keyParamName: "xAPIKey", configuration })

    
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            requestBeforeHook({
                queryParameters: localVarQueryParameter,
                requestConfig: localVarRequestOptions,
                path: localVarPath,
                configuration,
                pathTemplate: '/v1/health/{service}',
                httpMethod: 'GET'
            });

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * List the current health status of all services. Statuses update every 5 minutes. 
         * @summary list
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        list: async (options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/v1/health`;
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
            await setApiKeyToObject({ object: localVarHeaderParameter, key: "X-API-Key", keyParamName: "xAPIKey", configuration })

    
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            requestBeforeHook({
                queryParameters: localVarQueryParameter,
                requestConfig: localVarRequestOptions,
                path: localVarPath,
                configuration,
                pathTemplate: '/v1/health',
                httpMethod: 'GET'
            });

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * HealthApi - functional programming interface
 * @export
 */
export const HealthApiFp = function(configuration?: Configuration) {
    const localVarAxiosParamCreator = HealthApiAxiosParamCreator(configuration)
    return {
        /**
         * Look up the current health status of a specific service. Statuses update every 5 minutes. 
         * @summary get
         * @param {HealthApiGetRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async get(requestParameters: HealthApiGetRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<HealthResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.get(requestParameters.service, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * List the current health status of all services. Statuses update every 5 minutes. 
         * @summary list
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async list(options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<HealthResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.list(options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
    }
};

/**
 * HealthApi - factory interface
 * @export
 */
export const HealthApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = HealthApiFp(configuration)
    return {
        /**
         * Look up the current health status of a specific service. Statuses update every 5 minutes. 
         * @summary get
         * @param {HealthApiGetRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        get(requestParameters: HealthApiGetRequest, options?: AxiosRequestConfig): AxiosPromise<HealthResponse> {
            return localVarFp.get(requestParameters, options).then((request) => request(axios, basePath));
        },
        /**
         * List the current health status of all services. Statuses update every 5 minutes. 
         * @summary list
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        list(options?: AxiosRequestConfig): AxiosPromise<HealthResponse> {
            return localVarFp.list(options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for get operation in HealthApi.
 * @export
 * @interface HealthApiGetRequest
 */
export type HealthApiGetRequest = {
    
    /**
    * The name of the service to look up.
    * @type {string}
    * @memberof HealthApiGet
    */
    readonly service: string
    
}

/**
 * HealthApiGenerated - object-oriented interface
 * @export
 * @class HealthApiGenerated
 * @extends {BaseAPI}
 */
export class HealthApiGenerated extends BaseAPI {
    /**
     * Look up the current health status of a specific service. Statuses update every 5 minutes. 
     * @summary get
     * @param {HealthApiGetRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof HealthApiGenerated
     */
    public get(requestParameters: HealthApiGetRequest, options?: AxiosRequestConfig) {
        return HealthApiFp(this.configuration).get(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * List the current health status of all services. Statuses update every 5 minutes. 
     * @summary list
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof HealthApiGenerated
     */
    public list(options?: AxiosRequestConfig) {
        return HealthApiFp(this.configuration).list(options).then((request) => request(this.axios, this.basePath));
    }
}
