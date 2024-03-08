import os
import csv
from date_utils import get_current_date, convert_string_to_datetime
from constants import INJECTIONS_FIELDNAMES, DOSES_FIELDNAMES
from injection import Injection
from dose import Dose


class InjectionsFileHandler:
    """
    Class for reading/writing injections data from/to CSV file.

    Attributes:
        path (str): Path to a CSV file.
    """

    def __init__(self, path: str):
        self.path = path

    def read_todays_injections(self) -> list | None:
        """
        Reads the CSV file and returns a list of injections that were saved today.

        Returns:
            list: If there is at least one injection saved today.
            None: If there are no injections saved today.
        """
        if not os.path.exists(self.path):
            self.create_file_with_header()

        todays_injections = []
        with open(self.path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                date = convert_string_to_datetime(row["timestamp"]).date()
                if date == get_current_date():
                    datetime_timestamp = convert_string_to_datetime(row["timestamp"])
                    todays_injections.append(
                        Injection(row["type"], int(row["amount"]), datetime_timestamp)
                    )
        if not todays_injections:
            return None
        return todays_injections

    def save_new_injection(self, injection: Injection):
        """
        Saves newly added injection to a CSV file.

        Args:
            injection (Injection): Injection object to save.
        """
        write_header = False
        if not os.path.exists(self.path):
            write_header = True

        with open(self.path, "a", newline="") as file:
            writer = csv.DictWriter(file, INJECTIONS_FIELDNAMES)
            if write_header:
                writer.writeheader()
            writer.writerow(injection.to_dict())

    def create_file_with_header(self):
        with open(self.path, "w", newline="") as file:
            writer = csv.DictWriter(file, INJECTIONS_FIELDNAMES)
            writer.writeheader()


class DosesFileHandler:
    """
    Class for reading/updating insulin doses data from/to CSV file.

    Attributes:
        path (str): Path to a CSV file.
    """

    def __init__(self, path: str):
        self.path = path

    def read_doses(self) -> list:
        """
        Reads the CSV file and returns a list of insulin doses.

        Returns:
            list: A list of insulin doses.
        """
        if not os.path.exists(self.path):
            self.create_file_with_default_doses()

        doses = []
        with open(self.path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                doses.append(
                    Dose(
                        row["type"],
                        int(row["insulin_amount"]),
                        int(row["carbs_amount"]),
                    )
                )
        return doses

    def update_dose(self, dose: Dose):
        """
        Updates the insulin dose information and saves it to the CSV file.

        Args:
            dose (Dose): Insulin Dose object to save.
        """
        doses = self.read_doses()
        with open(self.path, "w", newline="") as file:
            writer = csv.DictWriter(file, DOSES_FIELDNAMES)
            writer.writeheader()
            for item in doses:
                if item.type == dose.type:
                    item = dose
                writer.writerow(item.to_dict())

    def create_file_with_default_doses(self):
        """
        If the CSV file does not exist, it creates it with the default values for the insulin doses.
        """
        short_dose = Dose("short", 1, 10)
        long_dose = Dose("long", 24, 0)

        with open(self.path, "w", newline="") as file:
            writer = csv.DictWriter(file, DOSES_FIELDNAMES)
            writer.writeheader()
            writer.writerow(short_dose.to_dict())
            writer.writerow(long_dose.to_dict())
