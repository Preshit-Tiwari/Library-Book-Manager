from ast import Try
from numb3rs import validate
import pytest

def test_input():
    assert validate("") == False
    assert validate("1.2.4.5") == True

def test_range():
    assert validate("274.1.4.5") == False
    assert validate("99.11.0.0") == True
    assert validate("20.260.15.35") == False

def test_ip4():
    assert validate("1.3.4.5") == True
    assert validate("12.3.44.56.98") == False
    assert validate("car") == False
