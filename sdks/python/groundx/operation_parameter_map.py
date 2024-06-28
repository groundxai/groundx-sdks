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
    '/v1/ingest/documents-GET': {
        'parameters': [
            {
                'name': 'n'
            },
            {
                'name': 'nextToken'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/v1/ingest/documents/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
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
                'name': 'n'
            },
            {
                'name': 'nextToken'
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
    '/v1/project/{projectId}/bucket/{bucketId}-POST': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'bucketId'
            },
        ]
    },
    '/v1/project-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'bucketName'
            },
        ]
    },
    '/v1/project/{projectId}-DELETE': {
        'parameters': [
            {
                'name': 'projectId'
            },
        ]
    },
    '/v1/project/{projectId}-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
        ]
    },
    '/v1/project-GET': {
        'parameters': [
            {
                'name': 'n'
            },
            {
                'name': 'nextToken'
            },
        ]
    },
    '/v1/project/{projectId}/bucket/{bucketId}-DELETE': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'bucketId'
            },
        ]
    },
    '/v1/project/{projectId}-PUT': {
        'parameters': [
            {
                'name': 'newName'
            },
            {
                'name': 'projectId'
            },
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