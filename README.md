# Diabetr - Manage Diabetes Better

## Setup and Installation

1. Clone this repository: `git clone https://github.com/beniusis/diabetr.git`
2. Navigate to the project's directory: `cd diabetr`
3. Create the virtual environment: `py -m venv .venv`
4. Activate the virtual environment:
   - If you're using Windows (PowerShell): `.venv/Scripts/Activate.ps1`
   - If you're using POSIX (bash/zsh): `source .venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Register _[here](https://calorieninjas.com)_ to get your `API` key from `CalorieNinjas`
7. Rename `rename_to.env` to `.env` and set your `API` key value to `NUTRITION_API_KEY`

## Usage

1. Menu only works with Linux and macOS. Try to run the program with this command: `main.py menu`.
2. If you're on Windows - run the program with arguments (e.g. `main.py add`)

```
Diabetr.
Running a program with menu only works in Linux and macOS.

Usage:
    main.py -h
    main.py menu
    main.py (add|calculate|doses|view)
    main.py update <type>

Commands:
    menu        Runs the program with the terminal menu functionality.
    add         Add the new injection.
    calculate   Calculates carbohydrates of a meal and informs the user with the amount of insulin to inject (suggestion).
    doses       View current insulin doses.
    view        View injections that were saved today.

Options:
    -h --help   Shows this screen.

Arguments:
    <type>      Insulin type (short, long).
```
