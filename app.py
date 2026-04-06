import json

FILE_NAME = "expenses.json"

def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))

    expenses = load_expenses()
    expense = {"name": name, "amount": amount}

    expenses.append(expense)

    save_expenses(expenses)

    print("Expense added successfully!")

def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return
    
    print("\nExpenses:")
    for i,expense in enumerate(expenses, start=1):
        print(f"{i}.{expense['name']} - ${expense['amount']}")


def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()