import json, csv

def load_expenses(filename="expenses.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("No existing expenses found. Starting with an empty list.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON file. Starting with an empty list.")
        return []


def save_expenses(expenses, filename="expenses.json"):
    with open(filename, "w") as f:
        json.dump(expenses, f, indent=4)

def export_to_csv(expenses, filename="expenses.csv"):
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["amount", "category", "description", "date"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)
