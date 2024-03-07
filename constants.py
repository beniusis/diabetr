NUTRITION_API_BASE_URL = "https://api.calorieninjas.com/v1/nutrition"
MAIN_MENU_OPTIONS = [
    "[1] Calculate Meal's Carbohydrates",
    "[2] View Current Insulin Doses",
    "[3] Change Short Insulin Dose",
    "[4] Change Long Insulin Dose",
    "[5] View Today's Injections",
    "[6] Create New Injection",
    "[7] Quit",
]
DATETIME_FORMAT = "%Y-%m-%d %H:%M"
INJECTIONS_FIELDNAMES = ["type", "amount", "timestamp"]
DOSES_FIELDNAMES = ["type", "insulin_amount", "carbs_amount"]
TABLE_STYLE = "rounded_grid"
NUTRIENTS_TABLE_HEADERS = ["Food", "Calories", "Fat", "Carbohydrates", "Protein"]
DOSES_TABLE_HEADERS = ["Type", "Insulin Amount", "For Amount of Carbohydrates"]
INJECTIONS_TABLE_HEADERS = ["Type", "Amount", "Date and Time"]
