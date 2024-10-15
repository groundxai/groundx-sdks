/*
GroundX APIs

RAG Made Simple, Secure and Hallucination Free

The version of the OpenAPI document: 1.3.26
Contact: support@eyelevel.ai

NOTE: This file is auto generated by Konfig (https://konfigthis.com).
*/
import type * as buffer from "buffer"


/**
 * 
 * @export
 * @interface SearchDocumentsRequest
 */
export interface SearchDocumentsRequest {
    /**
     * The search query to be used to find relevant documentation.
     * @type {string}
     * @memberof SearchDocumentsRequest
     */
    'query': string;
    /**
     * An array of unique documentIds to be searched.
     * @type {Array<string>}
     * @memberof SearchDocumentsRequest
     */
    'documentIds': Array<string>;
    /**
     * The minimum search relevance score required to include the result. By default, this is 10.0.
     * @type {number}
     * @memberof SearchDocumentsRequest
     */
    'relevance'?: number;
}
