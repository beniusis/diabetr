from helpers import calculate_insulin_amount_for_calculated_carbs
from dose import Dose


def test_calculate_insulin_amount_for_calculated_carbs_returns_correctly_rounded_value():
    mock_response = {
        "items": [
            {
                "name": "potatoes",
                "calories": 92.9,
                "fat_total_g": 0.1,
                "protein_g": 2.5,
                "carbohydrates_total_g": 21.0,
            },
            {
                "name": "orange juice",
                "calories": 46.4,
                "fat_total_g": 0.1,
                "protein_g": 0.7,
                "carbohydrates_total_g": 11.2,
            },
        ]
    }
    mock_dose = Dose("short", 1, 10)
    assert calculate_insulin_amount_for_calculated_carbs(mock_response, mock_dose) == 3

    mock_dose = Dose("short", 1, 15)
    assert calculate_insulin_amount_for_calculated_carbs(mock_response, mock_dose) == 2

    mock_dose = Dose("short", 1, 6)
    assert calculate_insulin_amount_for_calculated_carbs(mock_response, mock_dose) == 5
