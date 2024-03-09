"""
Diabetr.
Running a program with menu only works in Linux and macOS.

Usage:
    main.py -h
    main.py menu
    main.py (add|calculate|doses|view)
    main.py update <type>

Commands:
    menu            Runs the program with the terminal menu functionality.
    add             Add the new injection.
    calculate       Calculates carbohydrates of a meal and informs the user
                    with the amount of insulin to inject (suggestion).
    doses           View current insulin doses.
    view            View injections that were saved today.
    update <type>   Update the insulin dose (types: short, long).

Options:
    -h --help   Shows this screen.

Arguments:
    <type>      Insulin type (short, long).
"""

import helpers
from docopt import docopt


def main():
    helpers.clear_terminal()
    args = docopt(__doc__)
    if args["menu"]:
        helpers.with_menu()
    else:
        helpers.without_menu(args)


if __name__ == "__main__":
    main()
