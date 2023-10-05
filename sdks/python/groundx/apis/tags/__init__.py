# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from groundx.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    DOCUMENT = "Document"
    PROJECT = "Project"
    BUCKET = "Bucket"
    PREPROCESSOR = "Preprocessor"
    SEARCH = "Search"
    API_KEY_MANAGEMENT = "API Key Management"
