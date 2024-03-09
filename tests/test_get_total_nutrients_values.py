from helpers import get_total_nutrients_values


def test_get_total_nutrients_values_returns_correct_data():
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

    assert get_total_nutrients_values(mock_response) == [
        "Total",
        "139.3",
        "0.2",
        "32.2",
        "3.2",
    ]
