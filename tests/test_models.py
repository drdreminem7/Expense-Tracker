from models import Expense

def test_expense_to_dict():
    expense = Expense(date="2024-06-01", category="Food", amount=15.50, description="Lunch")
    result = expense.to_dict()
    assert result == {"date": "2024-06-01", "category": "Food", "amount": 15.50, "description": "Lunch"}
