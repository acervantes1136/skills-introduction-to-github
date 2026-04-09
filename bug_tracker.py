"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""

# This allows me to have access to the date/times and not type it out multiple times
from datetime import datetime

# Creates a new empty dictionary to store data afterwards
menu = {}

while True:
    user_choice = input(
        "Enter 'Add' to add a new menu item, or 'Quit' to stop editing menu: "
    ).title()

    if user_choice == "Add":
        # Gathering three pieces of information from User
        menu_item = input("Item name: ")
        description = input("Item description: ")
        price = input("Item price: ")

        # Shows timestamp after gathering inputs
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        """String format time formats the date and time
        Formatted in Year, Month, & Day/Hour, Minute, & Seconds"""
        # Store in dictionary (timestamp as key)
        menu[timestamp] = [menu_item, description, price]

        # Adds to bug_log.txt
        with open("bug_log.txt", "a") as file:
            file.write(
                f"""[{timestamp}]
Item: {menu_item}
Description: {description}
Price: {price:.2f}
--------------------------------------------------
"""
            )
    # This is the layout of the output after the user inputs 'Quit'

    # Once user inputs 'Quit' the loop ends and outputs the menu data
    elif user_choice == "Quit":
        print("Menu was saved successfully!")
        break

    else:
        print("Invalid input. Please enter 'Add' or 'Quit'.")
