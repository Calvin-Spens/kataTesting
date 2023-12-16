from problem_set_5 import shorten
from problem_set_5 import bank
from problem_set_2 import is_valid

def test_shorten():
    assert shorten("Why so Serious") == "Why s Srs"
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"

def test_bank():
    assert bank("Hello") == "$0"
    assert bank("Hello, Newman") == "$0"
    assert bank("How you doing?") == "$20"
    assert bank("What's happening?") == "$100"
    assert bank("Hellur, Newman") == "$20"

def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False

def test_fuel():
   ... 