# coding: utf-8


from typing import Optional, TypedDict

from groundx.apis.tags.customer_api import CustomerApi
from groundx.type.customer_response import CustomerResponse
from groundx.xray.logger import CustomLogger, setup_custom_logger


logger: CustomLogger = setup_custom_logger(__file__)


class Metric(TypedDict):
    max: int
    value: int


class Limits(TypedDict):
    fileTokens: Metric
    searches: Metric


DEFAULT_FILE_TOKENS = Metric(max=250000, value=0)
DEFAULT_SEARCH = Metric(max=100, value=0)

DEFAULT_LIMITS=Limits(fileTokens=DEFAULT_FILE_TOKENS, searches=DEFAULT_SEARCH)


class XRayLimits:
    def __init__(self, customer: CustomerApi):
        self.customer = customer
        self.limits: Limits = {
            "fileTokens": {"max": 0, "value": 0},
            "searches": {"max": 0, "value": 0},
        }

    def get_limits(self) -> Optional[Limits]:
        if (self.limits["fileTokens"]["max"] == 0 and self.limits["fileTokens"]["value"] == 0 and
            self.limits["searches"]["max"] == 0 and self.limits["searches"]["value"] == 0):
            return None

        return self.limits

    def update(self):
        self._load_limits()

    def _load_limits(self):
        resp = self.customer.get()
        self.limits = self._extract_limits(resp.body)

    def _extract_limits(self, response: CustomerResponse) -> Limits:
        if 'customer' not in response or not isinstance(response['customer'], dict):
            logger.warning("'customer' is missing, setting to default limits")
            return DEFAULT_LIMITS
        
        customer = response['customer']
        if 'subscription' not in customer or not isinstance(customer['subscription'], dict):
            logger.warning("'subscription' is missing, setting to default limits")
            return DEFAULT_LIMITS
        
        subscription = customer['subscription']
        if 'meters' not in subscription or not isinstance(subscription['meters'], dict):
            logger.warning("'meters' is missing, setting to default limits")
            return DEFAULT_LIMITS
        
        meters = subscription['meters']
        file_tokens = meters.get('fileTokens', DEFAULT_FILE_TOKENS)
        searches = meters.get('searches', DEFAULT_SEARCH)
        
        if not isinstance(file_tokens, dict):
            logger.warning("'fileTokens' is not a dictionary, setting to default limits")
            file_tokens = DEFAULT_FILE_TOKENS
        
        if not isinstance(searches, dict):
            logger.warning("'searches' is not a dictionary, setting to default limits")
            searches = DEFAULT_SEARCH
        
        file_tokens_max = file_tokens.get('max', 0)
        file_tokens_value = file_tokens.get('value', 0)
        searches_max = searches.get('max', 0)
        searches_value = searches.get('value', 0)
        
        return Limits(
            fileTokens=Metric(max=file_tokens_max, value=file_tokens_value),
            searches=Metric(max=searches_max, value=searches_value)
        )