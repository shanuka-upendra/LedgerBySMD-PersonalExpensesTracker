from cmath import exp

from models.expense import Expense
from utills.file_handler import load_expenses, save_expenses
from datetime import datetime


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")

    date = datetime.now().strftime("%Y-%m-%d")

    expense = Expense(name, amount, category, date)

    expenses = load_expenses()

    expenses.append(expense.to_dict())

    save_expenses(expenses)

    print("✅ Expense added successfully!")


def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\nExpenses List:")
    for i, exp in enumerate(expenses, start=1):
        print(
            f"{i}. "
            f"{exp['name']} | "
            f"${exp['amount']} | "
            f"{exp['category']} | "
            f"{exp['date']}"
        )


def delete_expense():
    expenses = load_expenses()

    if not expenses:
        print("No expenses to delete.")
        return

    print("\nExpenses List:")

    for i, exp in enumerate(expenses, start=1):
        print(
            f"{i}. "
            f"{exp['name']} | "
            f"${exp['amount']} | "
            f"{exp['category']} | "
            f"{exp['date']}"
        )

    try:
        index = int(input("Enter the number of the expense to delete: ")) - 1

        if 0 <= index < len(expenses):
            deleted = expenses.pop(index)
            save_expenses(expenses)

            print(f"✅ Deleted: {deleted['name']}")

        else:
            print("Invalid number. No expense deleted.")

    except ValueError:
        print("Invalid input. Please enter a number.")


def edit_expense():
    expenses = load_expenses()

    if not expenses:
        print("No expenses to edit.")
        return

    print("\nExpenses List:")

    for i, exp in enumerate(expenses, start=1):
        print(
            f"{i}. "
            f"{exp['name']} | "
            f"${exp['amount']} | "
            f"{exp['category']} | "
            f"{exp['date']}"
        )

    try:
        index = int(input("Enter the number of the expense to edit: ")) - 1

        if 0 <= index < len(expenses):
            name = input("Enter new expense name: ")
            amount = float(input("Enter new expense amount: "))
            category = input("Enter new expense category: ")

            expenses[index]["name"] = name
            expenses[index]["amount"] = amount
            expenses[index]["category"] = category

            save_expenses(expenses)

            print(f"✅ Edited: {name}")

        else:
            print("Invalid number. No expense edited.")

    except ValueError:
        print("Invalid input. Please enter a number.")


def show_total():
    expenses = load_expenses()

    total = sum(exp["amount"] for exp in expenses)

    print(f"\n💰 Total Expenses: ${total:.2f}:")


def filter_by_category():
    expenses = load_expenses()

    category = input("Enter category to filter:  ")

    filtered = [exp for exp in expenses if exp["category"].lower() == category.lower()]

    if not filtered:
        print("No expenses found for this category.")
        return

    print("\nFiltered Expenses:")

    for exp in filtered:
        print(
            f"{exp['name']} | "
            f"${exp['amount']} | "
            f"{exp['category']} | "
            f"{exp['date']}"
        )
