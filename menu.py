"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Program reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: break the dictionary into individual variables.
[ ] 6. Print each category and its details
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""

# PHASE 1: Create Menu File


def get_menu_options():
    menu = {}
    """This is where the user inputs items into each category
    to add to the menu"""
    while True:
        print("\n---Type 'Q' when done---")
        category = input("\nPlease input category to add to the menu: ").upper()
        """Typing 'Q' will end the loop and print out
        the menu file"""
        if category == "Q":
            break
        # Users will add each item dividing them by commas
        items = input("Please input items separated by commas only: ")
        menu[category] = items

    return menu


def save_to_file(menu):
    # Overwrite file each time for a clean submission
    with open("menu_config.txt", "w") as file:
        for category, items in menu.items():
            output = f"{category};{items}"
            file.write(output + "\n")


# This is where the user inputs are saved to the file and saved/printed to 'menu_config.txt'
def main():
    my_menu = get_menu_options()
    save_to_file(my_menu)
    print("Menu saved to menu_config.txt")


# PHASE 2: Read & Audit Menu

menus = {}


def read_menu():

    try:
        with open("menu_config.txt", "r") as file:
            for line in file:
                parts_of_line = line.strip().split(";")
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menus[category] = detail

    except FileNotFoundError:
        print("Error: menu_config.txt file not found.")
        return {}

    return menus


def split_into_variables(menu_items):
    # Breaking dictionary into individual variables
    appetizers = menu_items.get("APPETIZERS", "")
    entrees = menu_items.get("ENTREES", "")
    desserts = menu_items.get("DESSERTS", "")
    drinks = menu_items.get("DRINKS", "")

    return appetizers, entrees, desserts, drinks


# The user inputs will be added to the Menu Report with categories & their items listed
def print_menu(appetizers, entrees, desserts, drinks):

    print("\n------ MENU REPORT ------\n")

    print("APPETIZERS:")
    for item in appetizers.split(","):
        print(f"\t{item.strip()}")

    print("\nENTREES:")
    for item in entrees.split(","):
        print(f"\t{item.strip()}")

    print("\nDESSERTS:")
    for item in desserts.split(","):
        print(f"\t{item.strip()}")

    print("\nDRINKS:")
    for item in drinks.split(","):
        print(f"\t{item.strip()}")


# This is how the categories/items are going to be printed
def main():
    menu_items = read_menu()
    if menu_items:
        appetizers, entrees, desserts, drinks = split_into_variables(menu_items)
        print_menu(appetizers, entrees, desserts, drinks)


main()
