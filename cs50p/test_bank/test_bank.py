from bank import value

def test_empty():
    assert value("") == 100

def test_startwith_hello():
    assert value("hello") == 0
    assert value("HeLLO123") == 0
    assert value(":/hello") == 100
    assert value("HELLOOO!") == 0

def test_startwith_h():
    assert value("H") == 20
    assert value("hell11") == 20
    assert value(":hhhh:") == 100

