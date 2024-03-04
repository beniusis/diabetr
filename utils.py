import sys
from datetime import datetime
from data import BColors, InsulinType, InsulinDose, Injection
from constants import INSULIN_DOSE_MENU_OPTIONS, INSULIN_INJECTION_MENU_OPTIONS


def show_insulin_dose_menu():
    print(f"\n{BColors.HEADER}Insulin Dose Menu{BColors.ENDC}\n")
    for id, option in enumerate(INSULIN_DOSE_MENU_OPTIONS):
        print(f"{BColors.OKBLUE}{id + 1}. {option}{BColors.ENDC}")


def show_insulin_injection_menu():
    print(f"\n{BColors.HEADER}Insulin Injection Menu{BColors.ENDC}\n")
    for id, option in enumerate(INSULIN_INJECTION_MENU_OPTIONS):
        print(f"{BColors.OKBLUE}{id + 1}. {option}{BColors.ENDC}")


def get_menu_input():
    try:
        return int(input(BColors.OKCYAN + "\n>> " + BColors.ENDC))
    except KeyboardInterrupt:
        sys.exit()


def handle_insulin_dose_menu_input(input_value: int):
    if input_value == 1:
        InsulinDose.print_insulin_doses()
    elif input_value == 2:
        change_insulin_dose(InsulinDose.read_insulin_doses())
    elif input_value == 3:
        sys.exit()
    else:
        print(
            f"\n {BColors.WARNING}There is no selection with a number of{input_value}! {BColors.ENDC}\n"
        )


def change_insulin_dose(insulin_doses: dict):
    print()
    insulin_type = ask_user_for_insulin_type()
    insulin_dose_units = ask_user_for_insulin_dose_units()
    insulin_dose_carbs = ask_user_for_carbs(insulin_type)
    insulin_doses[insulin_type] = InsulinDose(
        insulin_type, insulin_dose_units, insulin_dose_carbs
    )
    InsulinDose.save_insulin_doses(insulin_doses)


def ask_user_for_insulin_type():
    while True:
        try:
            insulin_type = (
                input(
                    f"{BColors.HEADER}Enter type of insulin (short/long):{BColors.ENDC} "
                )
                .strip()
                .lower()
            )
            if insulin_type not in [InsulinType.SHORT.value, InsulinType.LONG.value]:
                raise ValueError(
                    f"{BColors.WARNING}Insulin type must be 'short' or 'long'!{BColors.ENDC}"
                )
            return insulin_type
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            sys.exit(
                f"\n{BColors.WARNING}Exited out of the program early.{BColors.ENDC}"
            )


def ask_user_for_insulin_dose_units():
    while True:
        try:
            insulin_dose_units = int(
                input(f"{BColors.HEADER}Enter units/ml:{BColors.ENDC} ")
            )
            if insulin_dose_units <= 0:
                raise ValueError
            return insulin_dose_units
        except ValueError:
            print(
                f"{BColors.WARNING}Insulin dose must be a valid number starting from 1!{BColors.ENDC}"
            )
        except KeyboardInterrupt:
            sys.exit(
                f"\n{BColors.WARNING}Exited out of the program early.{BColors.ENDC}"
            )


def ask_user_for_carbs(insulin_type):
    while True:
        try:
            insulin_dose_carbs = int(
                input(f"{BColors.HEADER}Enter carbs (g):{BColors.ENDC} ")
            )
            if insulin_dose_carbs < 0:
                raise ValueError
            elif insulin_dose_carbs == 0 and insulin_type == InsulinType.SHORT.value:
                raise ValueError
            return insulin_dose_carbs
        except ValueError:
            print(
                f"{BColors.WARNING}Carbs must be a valid number starting from 1 (or 0, if the insulin is of 'long' type)!{BColors.ENDC}"
            )
        except KeyboardInterrupt:
            sys.exit(
                f"\n{BColors.WARNING}Exited out of the program early.{BColors.ENDC}"
            )


def ask_user_for_injected_insulin_units():
    while True:
        try:
            injected_insulin_units = int(
                input(f"{BColors.HEADER}Injected units:{BColors.ENDC} ")
            )
            if injected_insulin_units <= 0:
                raise ValueError
            return injected_insulin_units
        except ValueError:
            print(
                f"{BColors.WARNING}Injected units must be a valid number and greater than 0!{BColors.ENDC}"
            )
        except KeyboardInterrupt:
            sys.exit(
                f"\n{BColors.WARNING}Exited out of the program early.{BColors.ENDC}"
            )


def handle_insulin_injection_menu_input(input_value):
    if input_value == 1:
        ...
    elif input_value == 2:
        add_insulin_injection()
    elif input_value == 3:
        sys.exit()
    else:
        print(
            f"\n {BColors.WARNING}There is no selection with a number of{input_value}! {BColors.ENDC}\n"
        )


def add_insulin_injection():
    insulin_type = ask_user_for_insulin_type()
    units_injected = ask_user_for_injected_insulin_units()
    date_timestamp = datetime.strptime(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S"
    )
    injection = Injection(insulin_type, units_injected, date_timestamp)
    injection.save()
