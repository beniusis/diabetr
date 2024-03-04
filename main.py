"""
Usage: main.py [-c|-d|-i]

Try:
    main.py -c
    main.py -d
    main.py -i

Options:
    -h --help       Show this screen.
    -c --calculate  Calculate carbohydrates in a meal.
    -d --dose       View and update data about the insulin doses.
    -i --injection  Save (mark) the insulin injection.
"""

import os
import utils
from docopt import docopt


def main():
    os.system("cls" if os.name == "nt" else "clear")
    args = docopt(__doc__)

    if args["--calculate"]:
        ...
    elif args["--dose"]:
        while True:
            utils.show_insulin_dose_menu()
            menu_number = utils.get_insulin_dose_menu_input()
            utils.handle_insulin_dose_menu_input(menu_number)
    elif args["--injection"]:
        ...


if __name__ == "__main__":
    main()
