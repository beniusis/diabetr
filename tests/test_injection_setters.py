import pytest
from injection import Injection
from date_utils import get_current_date_and_time
from datetime import datetime


def test_injection_type_setter_raises_value_error():
    with pytest.raises(ValueError):
        Injection("incorrect", 1, get_current_date_and_time())


def test_injection_amount_setter_raises_value_error():
    with pytest.raises(ValueError):
        Injection("short", "ten", get_current_date_and_time())

    with pytest.raises(ValueError):
        Injection("short", -2, get_current_date_and_time())

    with pytest.raises(ValueError):
        Injection("short", 0, get_current_date_and_time())


def test_injection_timestamp_setter_raises_value_error():
    with pytest.raises(ValueError):
        Injection("short", 1, datetime.now().isoformat())

    with pytest.raises(ValueError):
        Injection("short", 1, "Today")
