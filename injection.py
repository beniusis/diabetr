from dataclasses import dataclass
from datetime import datetime


@dataclass
class Injection:
    """
    Data class for storing information about the insulin injections.

    Attributes:
        type (str): Type of insulin (short, long).
        amount (int): Number of units per milliliter (units/ml) of insulin injected.
        timestamp (datetime): Date and time of injection.
    """

    type: str
    amount: int
    timestamp: datetime

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if type not in ["short", "long"]:
            raise ValueError("Insulin's type must be either 'short' or 'long'.")
        self._type = type

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount of insulin must be a positive number!")
        elif not type(amount) == int:
            raise ValueError("Amount of insulin must be a valid number!")
        self._amount = amount

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        if not type(timestamp) == datetime:
            raise ValueError(
                "Date and time of the injection must be a datetime object!"
            )
        self._timestamp = timestamp

    def to_dict(self):
        return {"type": self.type, "amount": self.amount, "timestamp": self.timestamp}
