import csv
import os
from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from constants import INSULIN_DOSE_FIELDNAMES, INJECTION_FIELDNAMES
from tabulate import tabulate


class BColors:
    """
    Color class to define the colors used in the terminal.
    """

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class InsulinType(Enum):
    """
    Enum class for representing the type of insulin.

    Attributes:
        SHORT (str): Short-acting insulin type.
        LONG (str): Long-acting insulin type.
    """

    SHORT = "short"
    LONG = "long"


@dataclass
class InsulinDose:
    """
    Data class for reading/changing insulin dose information.

    Attributes:
        insulin_type (str): Type of insulin.
        units_per_ml (int): Number of units per milliliter (units/ml) of insulin to inject.
        for_amount_of_carbs (int): Inject units_per_ml for this amount of carbohydrates (g).
    """

    insulin_type: str
    units_per_ml: int
    for_amount_of_carbs: int = 0

    @property
    def insulin_type(self):
        return self._insulin_type

    @insulin_type.setter
    def insulin_type(self, insulin_type):
        if insulin_type not in [InsulinType.SHORT.value, InsulinType.LONG.value]:
            raise ValueError("insulin_type must be either 'short' or 'long'")
        self._insulin_type = insulin_type

    @property
    def units_per_ml(self):
        return self._units_per_ml

    @units_per_ml.setter
    def units_per_ml(self, units_per_ml):
        if units_per_ml < 0 or units_per_ml == 0:
            raise ValueError("units_per_ml must be a positive number.")
        self._units_per_ml = units_per_ml

    @property
    def for_amount_of_carbs(self):
        return self._for_amount_of_carbs

    @for_amount_of_carbs.setter
    def for_amount_of_carbs(self, for_amount_of_carbs):
        if for_amount_of_carbs < 0:
            raise ValueError("for_amount_of_carbs must be a positive number.")
        elif for_amount_of_carbs == 0 and self.insulin_type == InsulinType.SHORT:
            raise ValueError(
                "for_amount_of_carbs cannot be equal to 0 if the insulin is "
                "of short type"
            )
        self._for_amount_of_carbs = for_amount_of_carbs

    def to_dict(self):
        return {
            "insulin_type": self.insulin_type,
            "units_per_ml": self.units_per_ml,
            "for_amount_of_carbs": self.for_amount_of_carbs,
        }

    @staticmethod
    def read_insulin_doses():
        insulin_doses = {}
        with open("files/insulin_dose.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                insulin_doses[row["insulin_type"]] = InsulinDose(
                    row["insulin_type"],
                    int(row["units_per_ml"]),
                    int(row["for_amount_of_carbs"]),
                )
        return insulin_doses

    @staticmethod
    def save_insulin_doses(insulin_doses: dict):
        with open("files/insulin_dose.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=INSULIN_DOSE_FIELDNAMES)
            writer.writeheader()
            for item in insulin_doses:
                writer.writerow(insulin_doses[item].to_dict())
        print(
            f"\n{BColors.OKGREEN}Insulin Doses has been saved successfully.{BColors.ENDC}"
        )

    @staticmethod
    def print_insulin_doses():
        insulin_doses = InsulinDose.read_insulin_doses()
        table_data = []
        for dose in insulin_doses:
            table_data.append(
                [
                    dose.capitalize(),
                    insulin_doses[dose].units_per_ml,
                    insulin_doses[dose].for_amount_of_carbs,
                ]
            )
        print(f"\n{BColors.BOLD}Information about the Insulin Doses{BColors.ENDC}\n")
        print(
            tabulate(
                table_data,
                headers=["Insulin Type", "Units/ml", "Carbs (g)"],
                tablefmt="rounded_grid",
            ),
        )


@dataclass
class Injection:
    """
    Data class for reading and creating insulin injection information.

    Attributes:
        insulin_type (str): Type of insulin.
        units_injected (int): Number of units of insulin to inject.
        date_timestamp (datetime): Date and time of injection.
    """

    insulin_type: str
    units_injected: int
    date_timestamp: datetime

    @property
    def insulin_type(self):
        return self._insulin_type

    @insulin_type.setter
    def insulin_type(self, insulin_type):
        if insulin_type not in [InsulinType.SHORT.value, InsulinType.LONG.value]:
            raise ValueError("insulin_type must be either 'short' or 'long'")
        self._insulin_type = insulin_type

    @property
    def units_injected(self):
        return self._units_injected

    @units_injected.setter
    def units_injected(self, units_injected):
        if units_injected <= 0:
            raise ValueError("units_injected must be a positive number.")
        self._units_injected = units_injected

    @property
    def date_timestamp(self):
        return self._date_timestamp

    @date_timestamp.setter
    def date_timestamp(self, date_timestamp):
        if not isinstance(date_timestamp, datetime):
            raise ValueError("date_timestamp must be a datetime object.")
        self._date_timestamp = date_timestamp

    def to_dict(self):
        return {
            "insulin_type": self.insulin_type,
            "units_injected": self.units_injected,
            "date_timestamp": self.date_timestamp,
        }

    @staticmethod
    def read_injections():
        if not os.path.exists("files/injections.csv"):
            raise FileNotFoundError("injections.csv file does not exist.")

        injections = []
        with open("files/injections.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                injections.append(
                    Injection(
                        row["insulin_type"],
                        row["units_injected"],
                        row["date_timestamp"],
                    )
                )
        return injections

    def save(self):
        if not os.path.exists("files/injections.csv"):
            with open("files/injections.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=INJECTION_FIELDNAMES)
                writer.writeheader()

        with open("files/injections.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=INJECTION_FIELDNAMES)
            writer.writerow(self.to_dict())

        print(
            f"{BColors.OKGREEN}Injection data has been saved successfully.{BColors.ENDC}"
        )
