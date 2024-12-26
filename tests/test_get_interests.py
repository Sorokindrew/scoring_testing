import pytest

from scoring.scoring import get_interests
from tests.fake import FakeStore


@pytest.mark.parametrize(
    ("cid", "result"),
    (
        ("1", ['hi-tech', 'geek']),
        ("2", ['geek', 'music']),
        ("3", ['tv', 'otus']),
        ("4", ['pets', 'books']),
        ("5", ['tv', 'books'])
    )
)
def test_get_interest_ok(cid, data, cached_data, result):
    fake_store = FakeStore(data=data, cached_data=cached_data)
    res = get_interests(store=fake_store, cid=cid)
    assert res == result

@pytest.mark.parametrize(
    ("cid", "result"),
    (
        ("6", []),
        ("7", []),
        ("8", []),
    )
)
def test_get_interests_negative(cid, result, data, cached_data):
    fake_store = FakeStore(data=data, cached_data=cached_data)
    res = get_interests(store=fake_store, cid=cid)
    assert res == result