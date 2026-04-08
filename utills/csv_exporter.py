import csv
from utills.file_handler import load_expenses


def export_to_csv():
    expenses = load_expenses()

    with open("data/expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "amount", "category", "date"])
        writer.writeheader()
        writer.writerows(expenses)

    print("✅ Expenses exported to expenses.csv successfully!")
