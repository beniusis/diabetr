from dataclasses import dataclass


@dataclass
class Food:
    """
    Data class for storing nutritional values of food.

    Attributes:
        name (str): Name of the food.
        calories (float): Calories (kcal).
        fat (float): Total fat (g).
        carbohydrates (float): Total carbohydrates (g).
        protein (float): Protein (g).
    """

    name: str
    calories: float
    fat: float
    carbohydrates: float
    protein: float

    def to_string_list(self):
        return [
            self.name,
            str(self.calories),
            str(self.fat),
            str(self.carbohydrates),
            str(self.protein),
        ]
