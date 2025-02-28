from seasons import date_to_minutes
import pytest

def test_correct_time():
    assert date_to_minutes("2020-07-17") == "Two million, two hundred ten thousand, four hundred minutes"


def test_valueError():
    with pytest.raises(SystemExit):
        date_to_minutes("january 15 2006")
    with pytest.raises(SystemExit):
        date_to_minutes("10-16-2004")
    with pytest.raises(SystemExit):
        date_to_minutes("16-10-2004")
    assert date_to_minutes("2000-10-16") == "Twelve million, five hundred ninety-eight thousand, five hundred sixty minutes"

