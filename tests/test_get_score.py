from datetime import datetime

import pytest

from scoring.scoring import get_score
from tests.fake import FakeStore


@pytest.mark.parametrize(
    ("phone", "email", "birthday", "gender", "first_name", "last_name", "count"),
    (
        ("79999999999", None, None, None, None, None, 1),
        ("79999999999", "test@test.net", None, None, None, None, 1),
        ("79999999999", "test@test.net", datetime(year=1990, month=1, day=1), None, None, None, 2),
        ("79999999999", "test@test.net", datetime(year=1990, month=1, day=1), 1, None, None, 2),
        ("79999999999", "test@test.net", datetime(year=1990, month=1, day=1), 1, "Andrey", None, 3),
        ("79999999999", "test@test.net", datetime(year=1990, month=1, day=1), 1, "Andrey", "Sorokin", 4),
     )
)
def test_get_score_save(data, cached_data, phone, email, birthday, gender, first_name, last_name, count):
    fake_store = FakeStore(data=data, cached_data=cached_data)
    get_score(
        store=fake_store,
        phone=phone,
        email=email,
        birthday=birthday,
        gender=gender,
        first_name=first_name,
        last_name=last_name,
    )
    assert len(fake_store.cached_data.keys()) == count

@pytest.mark.parametrize(
    ("phone", "email", "birthday", "gender", "first_name", "last_name", "count"),
    (
        ("79999999999", None, None, None, None, None, 3),
        ("79999999999", "test@test.net", None, None, None, None, 4),
        ("79999999999", "test@test.net", datetime(year=1990, month=1, day=1), None, None, None, 5),
        ("79999999999", "test@test.net", datetime(year=1990, month=1, day=1), 1, None, None, 6),
        ("79999999999", "test@test.net", datetime(year=1990, month=1, day=1), 1, "Andrey", None, 7),
        ("79999999999", "test@test.net", datetime(year=1990, month=1, day=1), 1, "Andrey", "Sorokin", 8),
     )
)
def test_get_score_get(data, cached_data, phone, email, birthday, gender, first_name, last_name, count):
    print(cached_data)
    fake_store = FakeStore(cached_data=cached_data, data=data)
    get_score(
        store=fake_store,
        phone=phone,
        email=email,
        birthday=birthday,
        gender=gender,
        first_name=first_name,
        last_name=last_name,
    )
    assert fake_store.received_cached == count
