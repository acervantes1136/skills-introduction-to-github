"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

# The Global Pantry
TOPPINGS = ("Pepperoni", "Mushrooms", "Onions", "Sausage", "Extra Cheese")

# Global constant sizes
SIZES = ("Small", "Medium", "Large")


# The 4 different Functions (Toppings)
def make_pizza(customer, size, topping, is_delivery=False):
    """Creates and displays the pizza order summary."""

    print("\n        Pizza Order Summary        ")
    print("-----------------------------------")
    print(f"{'Customer Name:':<20}{customer}")
    print(f"{'Pizza Size:':<20}{size}")
    print(f"{'Topping:':<20}{topping}")

    order_type = "Delivery" if is_delivery else "Pickup"
    print(f"{'Order Type:':<20}{order_type}")
    print("-----------------------------------\n")


def main():
    """Runs the pizza engine."""

    print("Welcome to The Resilient Pizza Engine!")
    print("Available Toppings:")
    for item in TOPPINGS:
        print(f"- {item}")

    # Collect user input
    customer_name = input("\nEnter customer name: ")

    # Size Validation Loop (Ensures user types in correct sizes)
    while True:
        pizza_size = input("Enter pizza size (Small/Medium/Large): ").title()
        if pizza_size in SIZES:
            break
        else:
            print("ERROR: Invalid size. Please choose Small, Medium, or Large.")

    # Topping Validation Loop
    while True:
        pizza_topping = input("Choose a topping from the list above: ").title()
        if pizza_topping in TOPPINGS:
            break
        else:
            print("Invalid topping. Please choose from the available list.")

    delivery_choice = input("Delivery? (yes/no): ").lower()
    delivery_bool = True if delivery_choice == "yes" else False

    # Using Keyword Arguments
    make_pizza(
        customer=customer_name,
        size=pizza_size,
        topping=pizza_topping,
        is_delivery=delivery_bool,
    )


# Program entry point
if __name__ == "__main__":
    main()
