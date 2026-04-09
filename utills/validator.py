def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount cannot be greater than 0. Please try again.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_valid_index(max_length):
    while True:
        try:
            index = int(input("Enter the number of the expense: ")) - 1
            if 0 <= index < max_length:
                return index
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Enter a valid number.")
