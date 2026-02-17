# Initial balance
balance = 1000.00
print("Where would you like to start today? ")

# Printed Menu
while True:
    print("\nMenu:")
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Exit")

        # User's choice
    choice = input("Enter your choice (1-5): ")

        # Match case choices
    match choice:
        case "1":
                print(f"Your current balance is: ${balance:,.2f}")

        case "2":
                amount_str = input("Enter deposit amount: ")
                if not amount_str.replace('.', '', 1).isdigit():
                    print("Invalid input. Please enter a numeric amount.")
                    continue
                amount = float(amount_str)
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
                balance += amount
                print(f"Deposited: ${amount:,.2f}")
                print(f"New balance: ${balance:,.2f}")

        case "3":
                amount_str = input("Enter withdrawal amount: ")
                if not amount_str.replace('.', '', 1).isdigit():
                    print("Invalid input. Please enter a numeric amount.")
                    continue
                amount = float(amount_str)
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
                if amount > balance:
                    print("Withdrawal exceeds balance.")
                    continue
                balance -= amount
                print(f"Withdrew: ${amount:,.2f}")
                print(f"New balance: ${balance:,.2f}")

        case "4":
                amount_str = input("Enter transfer amount: ")
                if not amount_str.replace('.', '', 1).isdigit():
                    print("Invalid input. Please enter a numeric amount.")
                    continue
                amount = float(amount_str)
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
                if amount > balance:
                    print("Transfer amount exceeds balance.")
                    continue
                balance -= amount
                print(f"Transferred: ${amount:,.2f}")
                print(f"New balance: ${balance:,.2f}")

        case "5":
                print("Thank you! Have a good day! Goodbye.")
                break

        case _:
                print("Invalid Selection. Please choose a valid option (1-5).")