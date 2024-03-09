import pytest
from dose import Dose


def test_dose_type_setter_raises_value_error():
    with pytest.raises(ValueError):
        Dose("incorrect", 1, 1)

    with pytest.raises(ValueError):
        Dose(10, 1, 1)


def test_dose_insulin_amount_setter_raises_value_error():
    with pytest.raises(ValueError):
        Dose("short", -2, 1)

    with pytest.raises(ValueError):
        Dose("long", 0, 0)

    with pytest.raises(ValueError):
        Dose("short", "ten", 1)


def test_dose_carbs_amount_setter_raises_value_error():
    with pytest.raises(ValueError):
        Dose("long", 20, "ten")

    with pytest.raises(ValueError):
        Dose("short", 5, 0)

    with pytest.raises(ValueError):
        Dose("short", 5, -2)
