from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("-1/3")
    assert convert("3/4") == 75

def test_gauge_e():
    assert gauge(1) == 'E'
def test_gauge_f():
    assert gauge(99) == "F"
def test_gauge_p():
    assert gauge(50) == "50%"
