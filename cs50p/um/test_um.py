from um import count
import pytest

def test_input():
    assert count("") == 0
    assert count("um") == 1
    assert count("car") == 0

def test_wordpart():
    assert count("hello ummmm umbrella") == 0
    assert count(" um it is good") == 1
    assert count("umum umm um") == 1

def test_case():
    assert count(" Um um um") == 3
    assert count("um, um? um!") == 3
    assert count("car") == 0
