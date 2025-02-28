from fuel import convert, gauge
import pytest

def test_zero_divivsion():
    with pytest.raises(ZeroDivisionError):
        convert('100/0')
    assert convert("2/2") == 100

def test_values():
    with pytest.raises(ZeroDivisionError):
        convert('100/0')
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("x/y")
    assert convert("1/2") == 50

def test_gauge():
    assert gauge(0.9) == "E"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99.9) == "F"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
