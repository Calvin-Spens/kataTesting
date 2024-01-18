from problem_set_5 import shorten
from problem_set_5 import bank
from problem_set_2 import is_valid
from problem_set_3 import fuel, tank_status
from lines_of_code import get_line_num

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
    assert fuel(75) == "75%"
    assert fuel(1) == "E"
    assert fuel(99) == "F"
    assert fuel(98) == "98%"
    assert fuel(2) == "2%"
    assert tank_status("1/4") == "0.25"
    assert tank_status("1/0") == 2
    assert tank_status("4/2") == 2
    assert tank_status("3/4") == "0.75"
    assert tank_status("4/4") == "1.00"
    assert tank_status("0/4") == "0.00"

def test_get_line_num():
    assert get_line_num("lines_of_code.py") == 23
    assert get_line_num("problem_set_4.py") == 144
    