import requests
import os
import sys
from tabulate import tabulate
from decouple import config
from colors import Colors
from food import Food
from date_utils import get_current_date_and_time
from dose import Dose
from injection import Injection
from file_handlers import DosesFileHandler, InjectionsFileHandler
from constants import (
    MAIN_MENU_OPTIONS,
    NUTRITION_API_BASE_URL,
    TABLE_STYLE,
    NUTRIENTS_TABLE_HEADERS,
    DOSES_TABLE_HEADERS,
    INJECTIONS_TABLE_HEADERS,
)

try:
    from simple_term_menu import TerminalMenu

    def init_main_menu() -> TerminalMenu:
        """
        Returns the TerminalMenu object for Main Menu.

        Returns:
            TerminalMenu: A Main Menu object.
        """
        return TerminalMenu(
            menu_entries=MAIN_MENU_OPTIONS,
            title="  Main Menu.\n  Press Q or Esc to Quit.\n",
            menu_highlight_style=("fg_red",),
            shortcut_brackets_highlight_style=("fg_red",),
            shortcut_key_highlight_style=("fg_red",),
        )

except NotImplementedError:
    pass


def clear_terminal():
    """
    Clears the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


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
            user_input = input(
                f"{Colors.HEADER}  Enter the food: {Colors.ENDC}"
            ).strip()
            if not user_input:
                raise ValueError
            return user_input
        except ValueError:
            print(f"{Colors.WARNING}  Food list cannot be empty!{Colors.ENDC}")


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


def get_formatted_food_list(response: dict) -> list | None:
    """
    Formats the list from the Nutrition Analysis API response values and returns it as a list.

    Returns:
        list: A list storing each item's nutrients values.
        None: If there are no items in the Nutrition Analysis API response.
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
    if not food_list:
        return None
    total_nutrients_list = get_total_nutrients_values(response)
    food_list.append(total_nutrients_list)
    return food_list


def print_table_of_nutrients(food_list: list | None):
    """
    Prints the table with the retrieved values of nutrients in the food list.

    Args:
        food_list (list | None): A list of food with nutrients values or None (if no items were found in the API's response).
    """
    if food_list == None:
        print(
            f"{Colors.WARNING}  Could not calculate the nutrients because the provided food input was unknown!{Colors.ENDC}\n"
        )
    else:
        print(tabulate(food_list, NUTRIENTS_TABLE_HEADERS, TABLE_STYLE))


def get_short_dose_data() -> Dose:
    """
    Gets and returns the short insulin data.

    Returns:
        Dose: An insulin dose object.
    """
    dfh = DosesFileHandler("files/doses.csv")
    doses = dfh.read_doses()

    for dose in doses:
        if dose.type == "short":
            return dose


def calculate_insulin_amount_for_calculated_carbs(response: dict, dose: Dose) -> int:
    """
    Calculates the insulin amount to inject based on the total carbohydrates in a meal.

    Args:
        response (dict): A Nutrition Analysis API response.
        dose (Dose): A short insulin dose object.

    Returns:
        int: Insulin amount to inject for a meal.
    """
    total_carbs = sum(item["carbohydrates_total_g"] for item in response["items"])
    return round(total_carbs / dose.carbs_amount * dose.insulin_amount)


def print_insulin_amount_for_calculated_carbs(insulin_amount: int):
    """
    Prints the amount of insulin to inject for a meal.

    Args:
        insulin_amount (int): Amount of insulin to inject.
    """
    print(
        f"\n{Colors.OKBLUE}  Inject this amount of insulin: {insulin_amount}{Colors.ENDC}\n"
    )


def init_carbs_calculation():
    """
    A function responsible for handling all of the calculation's logic and printing out the result into terminal.
    """
    try:
        food_input = ask_user_to_input_the_food()
        response = get_nutrition_analysis(food_input)
        food_list = get_formatted_food_list(response)
        print_table_of_nutrients(food_list)
        short_insulin_dose = get_short_dose_data()
        insulin_amount_to_inject = calculate_insulin_amount_for_calculated_carbs(
            response, short_insulin_dose
        )
        print_insulin_amount_for_calculated_carbs(insulin_amount_to_inject)
    except KeyboardInterrupt:
        pass


def print_table_of_doses(doses_list: list):
    """
    Prints the table with the information of current insulins doses.

    Args:
        doses_list (list): A list of current insulin doses.
    """
    print(tabulate(doses_list, DOSES_TABLE_HEADERS, TABLE_STYLE))


def init_show_doses():
    """
    A function responsible for handling all of the logic for printing out the current insulin doses information.
    """
    dfh = DosesFileHandler("files/doses.csv")
    doses = dfh.read_doses()
    print_table_of_doses(doses)


def print_table_of_todays_injections(injections_list: list | None):
    """
    Prints the table with the information of today's injections.

    Args:
        injections_list (list | None): A list of today's injections or None (if no injections were found).
    """
    if injections_list == None:
        print(f"{Colors.WARNING}  No injections were saved today!\n{Colors.ENDC}")
    else:
        print(tabulate(injections_list, INJECTIONS_TABLE_HEADERS, TABLE_STYLE))


def init_todays_injections():
    """
    A function responsible for handling all of the logic for showing today's injections data.
    """
    ifh = InjectionsFileHandler("files/injections.csv")
    injections = ifh.read_todays_injections()
    print_table_of_todays_injections(injections)


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
                f"{Colors.HEADER}  Enter the type of insulin (short, long): {Colors.ENDC}"
            )
            if not insulin_type:
                raise ValueError(
                    f"{Colors.WARNING}  Insulin type cannot be left empty!{Colors.ENDC}"
                )
            elif insulin_type not in ["short", "long"]:
                raise ValueError(
                    f"{Colors.WARNING}  Insulin's type must be either 'short' or 'long'.{Colors.ENDC}"
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
        ValueError: if `amount` is less than 0 or equal to 0.
    """
    while True:
        try:
            amount = int(input(f"{Colors.HEADER}  Amount of insulin: {Colors.ENDC}"))
            if not amount or amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print(
                f"{Colors.WARNING}  Amount of insulin must be a valid positive number!{Colors.ENDC}"
            )


def ask_the_user_to_input_the_carbs_amount() -> int:
    """
    Prompts the user to input the carbohydrates amount and returns its value.

    Returns:
        int: Number of carbohydrates (g).

    Raises:
        ValueError: if `amount` is empty.
        ValueError: if `amount` is less than 0.
    """
    while True:
        try:
            amount = int(
                input(
                    f"{Colors.HEADER}  Amount of carbohydrates (g) for amount of insulin to inject to: {Colors.ENDC}"
                )
            )
            if not amount or amount <= 0:
                raise ValueError
            return amount
        except ValueError as e:
            print(
                f"{Colors.WARNING}  Amount of carbohydrates must be a valid positive number!{Colors.ENDC}"
            )


def init_change_insulin_dose(type: str):
    """
    A function responsible for handling all of the logic for changing insulin dose data.

    Args:
        type (str): Insulin's type ('short', 'long').
    """
    try:
        dfh = DosesFileHandler("files/doses.csv")
        insulin_amount = ask_the_user_to_input_the_insulin_amount()
        carbs_amount = 0
        if type == "short":
            carbs_amount = ask_the_user_to_input_the_carbs_amount()
        dose = Dose(type, insulin_amount, carbs_amount)
        dfh.update_dose(dose)
        print(
            f"\n{Colors.OKGREEN}  {type.capitalize()} insulin dose has been successfully updated!{Colors.ENDC}\n"
        )
    except KeyboardInterrupt:
        pass


def init_add_injection():
    """
    A function responsible for handling all of the logic to save a newly added injection.
    """
    try:
        insulin_type = ask_the_user_to_input_the_insulin_type()
        insulin_amount = ask_the_user_to_input_the_insulin_amount()
        ifh = InjectionsFileHandler("files/injections.csv")
        current_datetime = get_current_date_and_time()
        injection = Injection(insulin_type, insulin_amount, current_datetime)
        ifh.save_new_injection(injection)
    except KeyboardInterrupt:
        pass


def with_menu():
    """
    Handles the main logic when the program is ran with terminal menu.
    """
    try:
        main_menu = init_main_menu()
    except NameError:
        sys.exit(
            f"{Colors.FAIL}Your OS is not supported to run the program with the menu.{Colors.ENDC}"
        )
    main_menu_exit = False

    while not main_menu_exit:
        selection = main_menu.show()
        clear_terminal()
        if selection == 0:
            init_carbs_calculation()
        elif selection == 1:
            init_show_doses()
        elif selection == 2:
            init_change_insulin_dose("short")
        elif selection == 3:
            init_change_insulin_dose("long")
        elif selection == 4:
            init_todays_injections()
        elif selection == 5:
            init_add_injection()
        elif selection == 6 or selection == None:
            main_menu_exit = True


def without_menu(args: dict):
    """
    Handles the main logic when the program is ran through CLI with arguments.
    """
    if args["calculate"]:
        init_carbs_calculation()
    elif args["doses"]:
        init_show_doses()
    elif args["update"]:
        insulin_type = args["<type>"].lower()
        if insulin_type not in ["short", "long"]:
            sys.exit(
                f"{Colors.FAIL}Insulin type must be either 'short' or 'long'.{Colors.ENDC}"
            )
        init_change_insulin_dose(insulin_type)
    elif args["view"]:
        init_todays_injections()
    elif args["add"]:
        init_add_injection()
