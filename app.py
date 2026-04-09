from services.expense_service import (
    add_expense,
    edit_expense,
    filter_by_category,
    filter_by_date,
    monthly_summary,
    show_total,
    view_expenses,
    delete_expense,
)
from utills.csv_exporter import (export_to_csv)


def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Edit Expense")
        print("5. Show Total Expenses")
        print("6. Filter by Category")
        print("7. Filter by Date")
        print("8. Monthly Summary")
        print("9. Export to csv")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            delete_expense()

        elif choice == "4":
            edit_expense()

        elif choice == "5":
            show_total()

        elif choice == "6":
            filter_by_category()

        elif choice == "7":
            filter_by_date()

        elif choice == "8":
            monthly_summary()

        elif choice == "9":
            export_to_csv()
        
        elif choice == "10":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
