from utils import get_non_empty_string, get_valid_float, get_valid_date, get_valid_id, get_valid_month

def test_get_non_empty_string(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Food")
    result = get_non_empty_string("category")
    assert result == "Food"

def test_get_non_empty_string_rejects_empty_then_accepts(monkeypatch):
    inputs = iter(["", "Food"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_non_empty_string("category")
    assert result == "Food"

def test_get_valid_float(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "15.5")
    result = get_valid_float("amount")
    assert result == 15.5

def test_get_valid_float_rejects_bad_then_accepts(monkeypatch): 
    inputs = iter(["hello", "-5", 0, "15.5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_valid_float("amount")
    assert result == 15.5  

def test_get_valid_id_acccepts_valid_id(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2")
    result = get_valid_id(3)
    assert result == 2

def test_get_valid_id_rejects_invalid_then_accepts(monkeypatch):
    inputs = iter(["abc", "99", "0", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_valid_id(3)
    assert result == 2

def test_get_valid_date_accepts_valid_date(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2023-05-15")
    result = get_valid_date()
    assert result == "2023-05-15"

def test_get_valid_month_accepts_valid_month(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2023-05")
    result = get_valid_month()
    assert result == "2023-05"