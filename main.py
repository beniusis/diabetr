"""
Diabetr.
Running a program with menu only works in Linux and macOS.

Usage:
    main.py -h
    main.py menu
    main.py (add|calculate|doses|view)
    main.py update <type>

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
