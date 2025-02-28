from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar1 = Jar()
    jar1.deposit(5)
    assert str(jar1) == "🍪🍪🍪🍪🍪"

def test_deposit():
    jar2 = Jar(15)
    jar2.deposit(10)
    assert jar2.size == 10
    with pytest.raises(ValueError):
        jar2.deposit(10)

def test_withdraw():
    jar3 = Jar(20)
    jar3.deposit(15)
    jar3.withdraw(10)
    assert jar3.size == 5
    with pytest.raises(ValueError):
        jar3.withdraw(10)
