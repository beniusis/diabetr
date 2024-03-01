# Diabetr - Manage Diabetes Better

## Setup and Installation

1. Clone this repository: `git clone https://github.com/beniusis/diabetr.git`
2. Navigate to the project's directory: `cd diabetr`
3. Create virtual environment: `py -m venv .venv`
4. Activate the virtual environment.

```
If you're using bash/zsh, run this command: source .venv/bin/activate
If you're using PowerShell (Windows), run this command: .venv/Scripts/Activate.ps1
If you're using PowerShell (POSIX), run this command: .venv/bin/Activate.ps1
```

5. Install the required dependencies: `pip install -r requirements.txt`
6. Register _[here](https://developer.edamam.com/edamam-nutrition-api)_ to get your `API` key from `edamam`
7. Rename `rename_to.env` to `.env` and set `NUTRITION_API_KEY` value to your `API` key
