from models.expense import Expense
from utills.file_handler import load_expenses, save_expenses
from datetime import datetime


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")

    date = datetime.now().strftime("%Y-%m-%d")

    expense = Expense(
        name,
        amount,
        category,
        date
    )

    expenses = load_expenses()

    expenses.append(
        expense.to_dict()
    )

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
    
    for i, exp in enumerate(expenses,start=1):
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
            
            print(
                f"✅ Deleted: {deleted['name']}"
            )
        
        else:
            print("Invalid number. No expense deleted.")
            
    except ValueError:
        print("Invalid input. Please enter a number.")