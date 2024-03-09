from helpers import get_formatted_food_list


def test_get_formatted_food_list_returns_correctly_formatted_list():
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

    expected_food_list = [
        ["Potatoes", "92.9", "0.1", "21.0", "2.5"],
        ["Orange Juice", "46.4", "0.1", "11.2", "0.7"],
        ["Total", "139.3", "0.2", "32.2", "3.2"],
    ]

    assert get_formatted_food_list(mock_response) == expected_food_list

    empty_mock_response = {"items": []}

    assert get_formatted_food_list(empty_mock_response) == None
