from numb3rs import validate

def test_validate_false():
    assert validate("192.168.001.1") == False
    assert validate("1.2.3.1000") == False
    assert validate("512.512.512.512") == False

def test_validate_string():
    assert validate("cat") == False

def test_validate_true():
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.100") == True
