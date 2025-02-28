from plates import is_valid

def test_startwith_2letters():
    assert is_valid("HELLO") == True
    assert is_valid("cs50") == True

def test_length():
    assert is_valid("CS5000000") == False
    assert is_valid("C") == False
    assert is_valid("CS") == True

def test_empty():
    assert is_valid("") == False

def test_puntuation():
    assert is_valid("Hello, world") == False
    assert is_valid("CS.#5") == False

def test_numbers():
    assert is_valid("CS05") == False
    assert is_valid("c5050") == False
    assert is_valid("AA22P") == False
    assert is_valid("PRT123") == True
