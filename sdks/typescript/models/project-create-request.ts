/*
GroundX API

Ground Your RAG Apps in Fact not Fiction

The version of the OpenAPI document: 1.0.0
Contact: support@groundx.ai

NOTE: This file is auto generated by Konfig (https://konfigthis.com).
*/
import type * as buffer from "buffer"


/**
 * 
 * @export
 * @interface ProjectCreateRequest
 */
export interface ProjectCreateRequest {
    /**
     * 
     * @type {string}
     * @memberof ProjectCreateRequest
     */
    'name': string;
    /**
     * Include a bucket name to automatically create a bucket and add it to this project
     * @type {string}
     * @memberof ProjectCreateRequest
     */
    'bucketName'?: string;
}

