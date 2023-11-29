/*
GroundX API

Ground Your RAG Apps in Fact not Fiction

The version of the OpenAPI document: 1.0.0
Contact: support@groundx.ai

NOTE: This file is auto generated by Konfig (https://konfigthis.com).
*/
import type * as buffer from "buffer"

import { DocumentType } from './document-type';

/**
 * 
 * @export
 * @interface DocumentLocalUploadRequestInnerMetadata
 */
export interface DocumentLocalUploadRequestInnerMetadata {
    /**
     * 
     * @type {number}
     * @memberof DocumentLocalUploadRequestInnerMetadata
     */
    'bucketId': number;
    /**
     * 
     * @type {string}
     * @memberof DocumentLocalUploadRequestInnerMetadata
     */
    'fileName': string;
    /**
     * 
     * @type {DocumentType}
     * @memberof DocumentLocalUploadRequestInnerMetadata
     */
    'fileType': DocumentType;
    /**
     * 
     * @type {object}
     * @memberof DocumentLocalUploadRequestInnerMetadata
     */
    'searchData'?: object;
}

