from datetime import datetime

def get_valid_float(field_name):
    while True:
        try:
            value = float(input(f"Enter expense {field_name}: "))
            if value <= 0:
                print(f"Invalid {field_name}. Please enter a number greater than 0.")
                continue
            else: return value
        except ValueError:
            print(f"Invalid {field_name}. Please enter a number")
    
def get_non_empty_string(field_name):
    while True:
        value = input(f"Enter expense {field_name}: ")
        if value.strip(): return value
        else: print(f"Invalid {field_name}. Please enter a non-empty string.")

def get_valid_date():
    while True:
        value = input("Enter expense date (YYYY-MM-DD): ")
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")
    

def get_valid_id(length):
    while True:
        try:
            expense_id = int(input("Enter the ID of the expense to delete: "))
            if 1 <= expense_id <= length:
                return expense_id
            else:
                print("Invalid ID. Please enter a valid expense ID.")
        except ValueError:
            print("Invalid ID. Please enter a valid expense ID.")

def get_valid_month():
    while True:
        value = input("Enter the month (YYYY-MM): ")
        try:
            datetime.strptime(value, "%Y-%m")
            return value
        except ValueError:
            print("Invalid month format. Please enter a month in the format YYYY-MM.")