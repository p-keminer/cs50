from plates import is_valid

def test_is_valid_len():
    assert is_valid("AAAAAAAAAA") == False

def test_is_valid_charbegin():
    assert is_valid("11111") == False

def test_is_valid_punctuation():
    assert is_valid("AS.20") == False

def test_is_valid_last():
    assert is_valid("AAA11A") == False

def test_is_valid_zero():
    assert is_valid("AAAA05") == False


