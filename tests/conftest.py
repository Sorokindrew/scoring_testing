import json

import pytest


@pytest.fixture
def data():
    return {
        "i:1" : json.dumps(['hi-tech', 'geek']),
        "i:2" : json.dumps(['geek', 'music']),
        "i:3" : json.dumps(['tv', 'otus']),
        "i:4" : json.dumps(['pets', 'books']),
        "i:5" : json.dumps(['tv', 'books']),
    }


@pytest.fixture(scope="module")
def cached_data():
    return {}

