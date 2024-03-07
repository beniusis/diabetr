import requests
from datetime import datetime
from datetime import date
from tabulate import tabulate
from decouple import config
from colors import Colors
from food import Food
from constants import (
    NUTRITION_API_BASE_URL,
    DATETIME_FORMAT,
    TABLE_STYLE,
    NUTRIENTS_TABLE_HEADERS,
    DOSES_TABLE_HEADERS,
    INJECTIONS_TABLE_HEADERS,
)


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


def ask_user_to_input_the_food() -> str:
    """
    Prompts the user to input the food and returns its value.

    Returns:
        str: Food list as a text.

    Raises:
        ValueError: if `user_input` is empty.
    """
    while True:
        try:
            user_input = input(f"{Colors.HEADER}Enter the food: {Colors.ENDC}").strip()
            if not user_input:
                raise ValueError
            return user_input
        except ValueError:
            print(f"{Colors.WARNING}Food list cannot be empty!{Colors.ENDC}")


def get_nutrition_analysis(query: str) -> dict | str:
    """
    Sends a request to Nutrition Analysis API and returns its response object.

    Args:
        query (str): Food list as a text.

    Returns:
        dict: Nutrition Analysis API response object.
        str: Error message if the request failed.
    """
    params = {"query": query}
    headers = {"X-Api-Key": config("NUTRITION_API_KEY")}

    try:
        response = requests.get(NUTRITION_API_BASE_URL, params=params, headers=headers)
        return response.json()
    except requests.RequestException as e:
        return e


def get_total_nutrients_values(response: dict) -> list:
    """
    Counts and returns the total values of nutrients in a list format.

    Returns:
        list: Total values of nutrients.
    """
    total_calories = sum(item["calories"] for item in response["items"])
    total_fat = sum(item["fat_total_g"] for item in response["items"])
    total_carbohydrates = sum(
        item["carbohydrates_total_g"] for item in response["items"]
    )
    total_protein = sum(item["protein_g"] for item in response["items"])
    return Food(
        "Total", total_calories, total_fat, total_carbohydrates, total_protein
    ).to_string_list()


def get_formatted_food_list(response: dict) -> list:
    """
    Formats the list from the Nutrition Analysis API response values and returns it as a list.

    Returns:
        list: A list storing each item's nutrients values.
    """
    food_list = []
    for item in response["items"]:
        food_list.append(
            Food(
                item["name"].title(),
                item["calories"],
                item["fat_total_g"],
                item["carbohydrates_total_g"],
                item["protein_g"],
            ).to_string_list()
        )
    total_nutrients_list = get_total_nutrients_values(response)
    food_list.append(total_nutrients_list)
    return food_list


def print_table_of_nutrients(food_list: list):
    """
    Prints the table with the retrieved values of nutrients in the food list.

    Args:
        food_list (list): A list of food with nutrients values.
    """
    print(tabulate(food_list, NUTRIENTS_TABLE_HEADERS, TABLE_STYLE))


def print_table_of_doses(doses_list: list):
    """
    Prints the table with the information of current insulins doses.

    Args:
        doses_list (list): A list of current insulin doses.
    """
    print(tabulate(doses_list, DOSES_TABLE_HEADERS, TABLE_STYLE))


def print_table_of_todays_injections(injections_list: list):
    """
    Prints the table with the information of today's injections.

    Args:
        injections_list (list): A list of today's injections.
    """
    print(tabulate(injections_list, INJECTIONS_TABLE_HEADERS, TABLE_STYLE))


def ask_the_user_to_input_the_insulin_type() -> str:
    """
    Prompts the user to input the insulin type and returns its value.

    Returns:
        str: Insulin type ('short' or 'long').

    Raises:
        ValueError: if `type` is not 'short' or 'long'.
    """
    while True:
        try:
            insulin_type = input(
                f"{Colors.HEADER}Enter the type of insulin (short, long): {Colors.ENDC}"
            )
            if not insulin_type:
                raise ValueError(
                    f"{Colors.WARNING}Insulin type cannot be left empty!{Colors.ENDC}"
                )
            elif insulin_type not in ["short", "long"]:
                raise ValueError(
                    f"{Colors.WARNING}Insulin's type must be either 'short' or 'long'.{Colors.ENDC}"
                )
            return insulin_type
        except ValueError as e:
            print(e)


def ask_the_user_to_input_the_insulin_amount() -> int:
    """
    Prompts the user to input the insulin amount and returns its value.

    Returns:
        int: Insulin amount (units/ml).

    Raises:
        ValueError: if `amount` is empty.
    """
    while True:
        try:
            amount = int(
                input(f"{Colors.HEADER}Amount of insulin injected: {Colors.ENDC}")
            )
            if not amount or amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print(
                f"{Colors.WARNING}Amount of insulin must be a valid positive number!{Colors.ENDC}"
            )
