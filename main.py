import os
import helpers
from simple_term_menu import TerminalMenu
from constants import MAIN_MENU_OPTIONS
from colors import Colors
from file_handlers import DosesFileHandler, InjectionsFileHandler
from injection import Injection


def main():
    os.system("cls" if os.name == "nt" else "clear")

    main_menu = TerminalMenu(
        menu_entries=MAIN_MENU_OPTIONS,
        title="  Main Menu.\n  Press Q or Esc to Quit.\n",
        menu_highlight_style=("fg_red",),
        shortcut_brackets_highlight_style=("fg_red",),
        shortcut_key_highlight_style=("fg_red",),
    )
    main_menu_exit = False

    while not main_menu_exit:
        selection = main_menu.show()
        if selection == 0:
            food_input = helpers.ask_user_to_input_the_food()
            response = helpers.get_nutrition_analysis(food_input)
            food_list = helpers.get_formatted_food_list(response)
            helpers.print_table_of_nutrients(food_list)
        elif selection == 1:
            dfh = DosesFileHandler("files/doses.csv")
            doses = dfh.read_doses()
            helpers.print_table_of_doses(doses)
        elif selection == 2:
            ...
        elif selection == 3:
            ...
        elif selection == 4:
            ifh = InjectionsFileHandler("files/injections.csv")
            injections = ifh.read_todays_injections()
            if injections == None:
                print(f"{Colors.WARNING}No injections were saved today!\n{Colors.ENDC}")
            else:
                helpers.print_table_of_todays_injections(injections)
        elif selection == 5:
            insulin_type_input = helpers.ask_the_user_to_input_the_insulin_type()
            amount_input = helpers.ask_the_user_to_input_the_insulin_amount()
            ifh = InjectionsFileHandler("files/injections.csv")
            current_datetime = helpers.get_current_date_and_time()
            injection = Injection(insulin_type_input, amount_input, current_datetime)
            ifh.save_new_injection(injection)
        elif selection == 6 or selection == None:
            main_menu_exit = True


if __name__ == "__main__":
    main()
