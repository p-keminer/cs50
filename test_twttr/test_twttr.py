from twttr import shorten

def test_shorten_A():
    assert shorten("A") == ""

def test_shorten_numbers():
    assert shorten("3") == "3"

def test_shorten_points():
     assert shorten(".:!") == ".:!"

def test_shorten_lower():
     assert shorten("twitter") == "twttr"

def test_shorten_upper():
     assert shorten("twwttr") == "twwttr"
