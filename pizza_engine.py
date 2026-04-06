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
"""These Global Constants make it easier to edit the code without having to search into your code/cause errors"""


# The 4 different Functions (Toppings)
def make_pizza(customer, size, topping, is_delivery=False):
    """Creates and displays the pizza order summary"""

    print("\n===================================")
    print("        Pizza Order Summary        ")
    print("===================================\n")

    print(f"Customer Name: {customer}")
    print(f"Pizza Size: {size}")
    print(f"Topping: {topping}")
    """The curly braces with the functions inside ensure the user input is being saved and shown in the order summary"""
    order_type = "Delivery" if is_delivery else "Pickup"
    print(f"Order Type: {order_type}")
    print("\n-----------------------------------\n")
    """The delivery is always false unless the user chooses 'Yes" """


def main():
    """Runs the pizza engine."""

    print("Welcome to Mia's Pizzeria!")
    print("Available Toppings:")
    for item in TOPPINGS:
        print(f"- {item}")
    """ 'item' is a place holder to list out the different TOPPINGS"""
    # Collect user input
    customer_name = input("\nEnter Your Name: ")

    # Size Validation Loop (Ensures user types in correct sizes)
    while True:
        pizza_size = input("Enter pizza size (Small/Medium/Large): ").title()
        if pizza_size in SIZES:
            break
            """The break stops with current loop and proceeds onto the next"""
        else:
            print("ERROR: Invalid size. Please choose Small, Medium, or Large.\n")
            """Unless user inputs an invalid size, the loop will restart by asking the question again"""

    # Topping Validation Loop
    while True:
        pizza_topping = input("Choose a topping from the list above: ").title()
        if pizza_topping in TOPPINGS:
            break
        else:
            print("ERROR: Invalid topping. Please choose from the available list.\n")

    delivery_choice = input("Delivery? (Yes/No): ").title()
    delivery_bool = True if delivery_choice == "Yes" else False
    """This boolean is starting off as 'false' from the start of the code; however, once the user types in 'Yes' it changes the boolean to 'True' """

    # Using Keyword Arguments
    make_pizza(
        customer=customer_name,
        size=pizza_size,
        topping=pizza_topping,
        is_delivery=delivery_bool,
    )
    """These keywords make it easier to code by plugging in all the inputs here, then plugging the key words into the codes output summary"""


# Program entry point
main()
"""This 'main()' function ties along with 'def' to ensure your code is in a single function making it easier to locate where your code starts and finishes"""
