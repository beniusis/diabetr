from dataclasses import dataclass


@dataclass
class Dose:
    """
    Data class for storing information about the current insulin doses.

    Attributes:
        type (str): Type of insulin (short, long).
        insulin_amount (int): Number of units per milliliter (units/ml) of insulin to inject.
        carbs_amount (int): For this amount of carbohydrates (g), inject this amount (insulin_amount) of insulin.
    """

    type: str
    insulin_amount: int
    carbs_amount: int

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if type not in ["short", "long"]:
            raise ValueError("Insulin's type must be either 'short' or 'long'.")
        self._type = type

    @property
    def insulin_amount(self):
        return self._insulin_amount

    @insulin_amount.setter
    def insulin_amount(self, insulin_amount):
        if insulin_amount <= 0:
            raise ValueError("Amount of insulin must be a positive number!")
        elif not type(insulin_amount) == int:
            raise ValueError("Amount of insulin must be a valid number!")
        self._insulin_amount = insulin_amount

    @property
    def carbs_amount(self):
        return self._carbs_amount

    @carbs_amount.setter
    def carbs_amount(self, carbs_amount):
        if carbs_amount < 0:
            raise ValueError("Amount of carbohydrates cannot be a negative number!")
        elif carbs_amount == 0 and self.type == "short":
            raise ValueError("Amount of carbohydrates must be a positive number!")
        elif not type(carbs_amount) == int:
            raise ValueError("Amount of carbohydrates must be a valid number!")
        self._carbs_amount = carbs_amount

    def to_dict(self):
        return {
            "type": self.type,
            "insulin_amount": self.insulin_amount,
            "carbs_amount": self.carbs_amount,
        }
