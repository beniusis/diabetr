from food import Food


def test_food_to_string_list_returns_correctly_formatted_list():
    food = Food("Potato", 20.5, 0.5, 2.5, 16.5)

    assert food.to_string_list() == ["Potato", "20.5", "0.5", "2.5", "16.5"]
