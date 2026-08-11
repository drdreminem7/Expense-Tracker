from utils import get_valid_float, get_non_empty_string, get_valid_date, get_valid_id, get_valid_month
from storage import load_expenses, save_expenses, export_to_csv
from models import Expense

expenses = [Expense(**expense) for expense in load_expenses()]

def add_expense():
    print("Adding an expense:")
    amount = get_valid_float("amount")
    category = get_non_empty_string("category")
    description = get_non_empty_string("description")
    date = get_valid_date()

    expenses.append(Expense(date, category, amount, description))
    save_expenses([expense.to_dict() for expense in expenses])
    print("Done adding expense.")

def list_expenses():
    print(f"{"ID":<2} | {"Date":<10} | {"Category":<12} | {"Amount":<8} | {"Description":<20}")
    print("-" * 56)
    for i, expense in enumerate(expenses, start=1):
        print(f"{i:<2} | {expense.date:<10} | {expense.category:<12} | {expense.amount:<8} | {expense.description:<20}")
    print("\n")

def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return
    
    list_expenses()

    expense_id = get_valid_id(len(expenses))
    print(f"Deleted: {expenses[expense_id - 1].category} - {expenses[expense_id - 1].amount}")
    expenses.pop(expense_id - 1)
    save_expenses([expense.to_dict() for expense in expenses])

def monthly_total():
    month = get_valid_month()

    total = 0
    for expense in expenses:
        if expense.date.startswith(month):
            total += expense.amount

    if total == 0:
        print(f"No expenses found for {month}.")
    else:
        print(f"Monthly total for {month}: {total:.2f}")

def filter_by_category(category):
    filtered = [expense for expense in expenses if expense.category.lower() == category.lower()]
    print("Expenses filtered by category: " + category)
    print(f"{"ID":<2} | {"Date":<10} | {"Category":<12} | {"Amount":<8} | {"Description":<20}")
    print("-" * 56)
    for i, expense in enumerate(filtered, start=1):
        print(f"{i:<2} | {expense.date:<10} | {expense.category:<12} | {expense.amount:<8} | {expense.description:<20}")
    print("\n")

def main():
    print("Expense Tracker\n")

    while True:
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Delete Expense")
        print("4. Monthly Total")
        print("5. Export to CSV")
        print("6. Filter by Category")
        print("7. Exit\n")
        choice = input("Choose: ")
        match choice:
            case "1":
                add_expense()
            case "2":
                list_expenses()
            case "3":
                delete_expense()
            case "4":
                monthly_total()
            case "5":
                export_to_csv([expense.to_dict() for expense in expenses])
                print("Expenses exported to expenses.csv")
            case "6":
                filter_by_category(get_non_empty_string("category"))
            case "7":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



