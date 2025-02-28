from twttr import shorten

def test_empty():
    assert shorten("") == ""

def test_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("preshit") =="prsht"

def test_consonent():
    assert shorten("ABCD") == "BCD"
    assert shorten("hiii") == "h"

def test_numbers():
    assert shorten("pres123") == "prs123"
    assert shorten("11235") == "11235"

def test_puntuations():
    assert shorten("hello,world") == "hll,wrld"
    assert shorten("cs50!") == "cs50!"
