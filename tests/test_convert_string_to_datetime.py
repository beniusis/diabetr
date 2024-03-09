from date_utils import convert_string_to_datetime
from datetime import datetime


def test_convert_string_to_datetime_returns_correctly_formatted_datetime_object():
    date_string = "2024-03-08 15:35"
    assert convert_string_to_datetime(date_string) == datetime(2024, 3, 8, 15, 35)
