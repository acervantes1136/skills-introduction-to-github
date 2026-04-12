"""
-----------------------------------------------------------------------
ASSIGNMENT 11A: THE OFFICE HERO DASHBOARD
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constants OFFICE_NAME and TAX_RATE defined in ALL_CAPS.
[ ] 3. Function 'process_expenses' returns TWO values (float, string).
[ ] 4. main() function uses try/except for numeric price/qty inputs.
[ ] 5. main() calls function using KEYWORD ARGUMENTS.
[ ] 6. main() correctly unpacks and prints both return values.
-----------------------------------------------------------------------
"""

# Global Constants
OFFICE_NAME = "Vortex Industries"
TAX_RATE = 0.05


def process_expenses(item_name, price, quantity):
    """
    Calculates subtotal, tax, and final total
    & Returns final_total (float) & summary (string)
    """
    subtotal = price * quantity
    tax = subtotal * TAX_RATE
    final_total = subtotal + tax

    # This is what the user sees (like a receipt) as their output
    summary = (
        f"----------------------------------------------"
        f"\n     Expense Summary for {OFFICE_NAME}     \n"
        f"----------------------------------------------"
        f"\nItem: {item_name}\n"
        f"Price: ${price:.2f}\n"
        f"Quantity: {quantity}\n"
        f"Subtotal: ${subtotal:.2f}\n"
        f"Tax (5%): ${tax:.2f}\n"
        f"Final Total: ${final_total:.2f}"
        f"\n----------------------------------------------"
    )

    return final_total, summary


def main():
    print(f"\n     {OFFICE_NAME} Expense Dashboard     \n")
    """This is where the user is imputing their information
    to add information into the 'summary' code"""

    # This while loop ensures the loop won't end if the user enters the wrong input
    while True:
        item_name = input("Enter item name: ")

        try:
            price = float(input("Enter item price: "))
            quantity = int(input("Enter quantity (Amount): "))
            break
        except ValueError:
            print("ERROR: Price must be a number/quantity must be an integer.")
            print("Try Again.\n")

    # Function calling for keyword arguments
    final_amount, summary_string = process_expenses(
        item_name=item_name, price=price, quantity=quantity
    )

    # Unpacking and printing both return values
    print(summary_string)
    print(f"\nReturned Final Value: ${final_amount:.2f}")


main()
