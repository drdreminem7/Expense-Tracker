from storage import load_expenses, save_expenses, export_to_csv
import csv

def test_loading_and_saving_expenses(tmp_path):
    temp_file = tmp_path / "temp_expenses.json"
    expenses = [{"date": "2024-06-01", "category": "Food", "amount": 15.50, "description": "Lunch"}]
    save_expenses(expenses, filename=temp_file)
    loaded_expenses = load_expenses(filename=temp_file)
    assert loaded_expenses == expenses

def test_loading_expenses_with_invalid_json(tmp_path):
    temp_file = tmp_path / "invalid_expenses.json"
    temp_file.write_text("invalid json")
    loaded_expenses = load_expenses(filename=temp_file)
    assert loaded_expenses == []

def test_exporting_to_csv(tmp_path):
    temp_file = tmp_path / "temp_expenses.csv"
    expenses = [{"date": "2024-06-01", "category": "Food", "amount": 15.50, "description": "Lunch"}]
    export_to_csv(expenses, filename=temp_file)

    with open(temp_file, 'r') as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == ["amount", "category", "description", "date"]
        for row in reader:
            assert row["date"] == "2024-06-01"
            assert row["category"] == "Food"
            assert row["amount"] == "15.5"
            assert row["description"] == "Lunch"

