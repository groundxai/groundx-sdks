operation_parameter_map = {
    '/v1/bucket-POST': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/v1/bucket/{bucketId}-DELETE': {
        'parameters': [
            {
                'name': 'bucketId'
            },
        ]
    },
    '/v1/bucket/{bucketId}-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
        ]
    },
    '/v1/bucket-GET': {
        'parameters': [
            {
                'name': 'n'
            },
            {
                'name': 'nextToken'
            },
        ]
    },
    '/v1/bucket/{bucketId}-PUT': {
        'parameters': [
            {
                'name': 'newName'
            },
            {
                'name': 'bucketId'
            },
        ]
    },
    '/v1/customer-GET': {
        'parameters': [
        ]
    },
    '/v1/ingest/documents/website-POST': {
        'parameters': [
            {
                'name': 'websites'
            },
        ]
    },
    '/v1/ingest/documents-DELETE': {
        'parameters': [
            {
                'name': 'documentIds'
            },
        ]
    },
    '/v1/ingest/document/{documentId}-DELETE': {
        'parameters': [
            {
                'name': 'documentId'
            },
        ]
    },
    '/v1/ingest/document/{documentId}-GET': {
        'parameters': [
            {
                'name': 'documentId'
            },
        ]
    },
    '/v1/ingest/{processId}-GET': {
        'parameters': [
            {
                'name': 'processId'
            },
        ]
    },
    '/v1/ingest/documents/local-POST': {
        'parameters': [
        ]
    },
    '/v1/ingest/documents/remote-POST': {
        'parameters': [
            {
                'name': 'documents'
            },
        ]
    },
    '/v1/ingest/documents-GET': {
        'parameters': [
            {
                'name': 'n'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'sortOrder'
            },
            {
                'name': 'status'
            },
            {
                'name': 'nextToken'
            },
        ]
    },
    '/v1/ingest/documents/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'n'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'sortOrder'
            },
            {
                'name': 'status'
            },
            {
                'name': 'nextToken'
            },
        ]
    },
    '/v1/group/{groupId}/bucket/{bucketId}-POST': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': 'bucketId'
            },
        ]
    },
    '/v1/group-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'bucketName'
            },
        ]
    },
    '/v1/group/{groupId}-DELETE': {
        'parameters': [
            {
                'name': 'groupId'
            },
        ]
    },
    '/v1/group/{groupId}-GET': {
        'parameters': [
            {
                'name': 'groupId'
            },
        ]
    },
    '/v1/group-GET': {
        'parameters': [
            {
                'name': 'n'
            },
            {
                'name': 'nextToken'
            },
        ]
    },
    '/v1/group/{groupId}/bucket/{bucketId}-DELETE': {
        'parameters': [
            {
                'name': 'groupId'
            },
            {
                'name': 'bucketId'
            },
        ]
    },
    '/v1/group/{groupId}-PUT': {
        'parameters': [
            {
                'name': 'newName'
            },
            {
                'name': 'groupId'
            },
        ]
    },
    '/v1/health/{service}-GET': {
        'parameters': [
            {
                'name': 'service'
            },
        ]
    },
    '/v1/health-GET': {
        'parameters': [
        ]
    },
    '/v1/search/{id}-POST': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'id'
            },
            {
                'name': 'relevance'
            },
            {
                'name': 'n'
            },
            {
                'name': 'nextToken'
            },
            {
                'name': 'verbosity'
            },
        ]
    },
    '/v1/search/documents-POST': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'documentIds'
            },
            {
                'name': 'relevance'
            },
            {
                'name': 'n'
            },
            {
                'name': 'nextToken'
            },
            {
                'name': 'verbosity'
            },
        ]
    },
};