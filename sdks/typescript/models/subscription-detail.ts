/*
GroundX APIs

RAG Made Simple, Secure and Hallucination Free

The version of the OpenAPI document: 1.3.26
Contact: support@eyelevel.ai

NOTE: This file is auto generated by Konfig (https://konfigthis.com).
*/
import type * as buffer from "buffer"

import { SubscriptionDetailMeters } from './subscription-detail-meters';

/**
 * Subscription information for the user, including current usage and limits
 * @export
 * @interface SubscriptionDetail
 */
export interface SubscriptionDetail {
    /**
     * 
     * @type {SubscriptionDetailMeters}
     * @memberof SubscriptionDetail
     */
    'meters'?: SubscriptionDetailMeters;
}

