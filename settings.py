ELASTICSEARCH_URL = 'http://127.0.0.1:9200/'
ELASTICSEARCH_INDEX = 'abonent'
RESOURCE_METHODS = ['GET']

schema = {
    "entry_id": {"type" : "text"},
    "full_name": {"type" : "text"},
    "address": {"type" : "text"},
    "phone": {"type" : "list"},
    "year": {"type" : "integer"}
}

abonent = {
    'item_title': 'abonent',
    'resource_methods': ['GET'],
    'schema': schema
}

DOMAIN = {
    'abonent': abonent,
    'datasource': {
        'backend': 'elastic'
    }
}

