from seasons import sing_minutes
from datetime import date
import pytest

def test_sing_minutes_r():
    assert sing_minutes(date.fromisoformat("2025-05-18")) == "Five hundred twenty-five thousand, six hundred minutes"
    assert sing_minutes(date.fromisoformat("2024-05-18")) == "One million, fifty-one thousand, two hundred minutes"

def test_sing_minutes_f():
    with pytest.raises(ValueError):
        sing_minutes(date.fromisoformat("2024.05.18"))
