# diabetr

diabetr is a command-line interface (CLI) application that helps with meal's carbohydrates, insulin dose calculation and tracks insulin injections.

## Table of Contents

- [Overview](#overview)
  - [Features](#features)
  - [Technologies and Tools](#technologies-and-tools)
- [Setup and Usage](#setup-and-usage)
  - [Setup](#setup)
  - [Usage](#usage)

## Overview

### Features

- Run the program with the terminal menu functionality (Linux & macOS only).
- Calculate meal's carbohydrates by entering the food and its quantity (e.g. 150g potatoes, 250g cooked chicken, etc.).
- Automatically calculate insulin dose for a meal based on the set dosage.
- Update the insuling dosage (short and long lasting insulin separately).
- Save new injections and view injections that were saved on current day.

### Technologies and Tools

- 🐍 **Language**: [Python](https://www.python.org)
- 🔎 **Unit Tests**: [pytest](https://docs.pytest.org)
- 📦 **Packages**: [docopt](https://pypi.org/project/docopt/), [simple-term-menu](https://pypi.org/project/simple-term-menu), [tabulate](https://pypi.org/project/tabulate)

## Setup and Usage

### Setup

1. Clone this repository:

```sh
git clone https://github.com/beniusis/diabetr.git
```

2. Navigate to the project's root directory

```sh
cd diabetr
```

3. Create the virtual environment:

```sh
py -m venv .venv
```

4. Activate the virtual environment:

_Windows (PowerShell)_

```sh
.venv/Scripts/Activate.ps1
```

_POSIX (bash/zsh)_

```sh
source .venv/bin/activate
```

5. Install the required dependencies:

```sh
pip install -r requirements.txt
```

6. Register [_here_](https://calorieninjas.com) to get your `API` key from `CalorieNinjas`

7. Rename `rename_to.env` to `.env` and set your `API` key value to `NUTRITION_API_KEY`

### Usage

1. Run the program with _terminal menu_ (Linux & macOS only):

```sh
py main.py menu
```

2. Run the program with _arguments_:

```
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
```
