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
 * @interface DocumentRemoteUploadRequestDocumentsInner
 */
export interface DocumentRemoteUploadRequestDocumentsInner {
    /**
     * the bucketId of the bucket which this remote file will be uploaded to.
     * @type {number}
     * @memberof DocumentRemoteUploadRequestDocumentsInner
     */
    'bucketId': number;
    /**
     * The name of the file being uploaded
     * @type {string}
     * @memberof DocumentRemoteUploadRequestDocumentsInner
     */
    'fileName'?: string;
    /**
     * The type of document (one of the seven currently supported file types)
     * @type {DocumentType}
     * @memberof DocumentRemoteUploadRequestDocumentsInner
     */
    'fileType'?: DocumentType;
    /**
     * Custom metadata which can be used to influence GroundX\'s search functionality. This data can be used to further hone GroundX search.
     * @type {object}
     * @memberof DocumentRemoteUploadRequestDocumentsInner
     */
    'searchData'?: object;
    /**
     * The URL of the document being uploaded to GroundX.
     * @type {string}
     * @memberof DocumentRemoteUploadRequestDocumentsInner
     */
    'sourceUrl': string;
}

