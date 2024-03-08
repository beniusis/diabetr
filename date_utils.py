from datetime import datetime
from datetime import date
from constants import DATETIME_FORMAT


def convert_string_to_datetime(date_string: str) -> datetime:
    """
    Converts the date string into a datetime in format YYYY-MM-DD HH:MM:00.

    Args:
        date_string (str): Date and time string.

    Returns:
        datetime: Datetime in format YYYY-MM-DD HH:MM:00.
    """
    return datetime.fromisoformat(date_string)


def get_current_date_and_time() -> datetime:
    """
    Gets the current date and time.

    Returns:
        datetime: Current date and time in format YYYY-MM-DD HH:MM:00.
    """
    current_date_string = datetime.now().strftime(DATETIME_FORMAT)
    return datetime.strptime(current_date_string, DATETIME_FORMAT)


def get_current_date() -> date:
    """
    Gets the current date.

    Returns:
        date: Today's date in format YYYY-MM-DD.
    """
    return date.today()
