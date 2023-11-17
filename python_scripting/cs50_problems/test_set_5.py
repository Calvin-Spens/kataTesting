from problem_set_5 import shorten
from problem_set_5 import bank

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