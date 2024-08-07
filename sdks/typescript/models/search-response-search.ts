/*
GroundX APIs

RAG Made Simple, Secure and Hallucination Free

The version of the OpenAPI document: 1.3.26
Contact: support@eyelevel.ai

NOTE: This file is auto generated by Konfig (https://konfigthis.com).
*/
import type * as buffer from "buffer"

import { SearchResultItem } from './search-result-item';

/**
 * 
 * @export
 * @interface SearchResponseSearch
 */
export interface SearchResponseSearch {
    /**
     * Total results
     * @type {number}
     * @memberof SearchResponseSearch
     */
    'count'?: number;
    /**
     * Search results
     * @type {Array<SearchResultItem>}
     * @memberof SearchResponseSearch
     */
    'results'?: Array<SearchResultItem>;
    /**
     * The original search request query
     * @type {string}
     * @memberof SearchResponseSearch
     */
    'query'?: string;
    /**
     * Confidence score in the search results
     * @type {number}
     * @memberof SearchResponseSearch
     */
    'score'?: number;
    /**
     * The actual search query, if the search request query was re-written
     * @type {string}
     * @memberof SearchResponseSearch
     */
    'searchQuery'?: string;
    /**
     * Suggested context for LLM completion
     * @type {string}
     * @memberof SearchResponseSearch
     */
    'text'?: string;
    /**
     * For paginated results
     * @type {string}
     * @memberof SearchResponseSearch
     */
    'nextToken'?: string;
}

