"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")


# TODO: Define get_price(size)
def get_price(size):
    # Determine price based on size
    if size == "Small":
        return 3.00
    elif size == "Medium":
        return 4.00
    else:
        return 5.00


# TODO: Define blend(size, base, fruit, scoops)
def blend(size, base, fruit, scoops):
    # This will show the final order display
    print("\n   Smoothie Order   ")
    print(f"Size: {size}")
    print(f"Base: {base}")
    print(f"Fruit: {scoops} scoop(s) of {fruit}.")


def main():
    print("Welcome to Smoothie Queen!")
    # User inputs what 'base' and 'fruit' they want
    choice_size = input("Size (Small/Medium/Large): ").title().strip()
    choice_base = input("Select Base: ").title()
    choice_fruit = input("Select Fruit: ").title()
    # User error by typing in anything other than integer
    try:
        scoops = int(input("How many scoops of Fruit? "))
    except ValueError:
        # Automatically puts in '1'
        print("Invalid entry. Defaulting to 1.")
        scoops = 1

    # TODO: Define main() to collect input and call your logic
    # Outputting price by size
    cost = get_price(choice_size)

    # Call the smoothie function
    blend(choice_size, choice_base, choice_fruit, scoops)

    print(f"Total: ${cost:.2f}")


# Run back the system
main()
