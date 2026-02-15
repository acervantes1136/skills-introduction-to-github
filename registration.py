"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 4 inputs have 'while' loop validation.
[ ] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[ ] 4. I have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

# Users First & Last Name
first_name = input("\nEnter First Name: ")
while first_name == "":
    print("⚠️ INVALID: Name cannot be blank.")
    first_name = input("Please enter First Name: ")
last_name = input("Enter Last Name: ")
while last_name == "":
    print("⚠️ INVALID: Name cannot be blank.")
    last_name = input("Please enter Last Name: ")

# Chaperone Status
chaperone = input("\nParent volunteering to chaperone? (Y/N): ").upper()
while chaperone != "Y" and chaperone != "N":
    print("⚠️ INVALID: Please enter either Y or N.")
    chaperone = input("Parent volunteering to chaperone? (Y/N): ").upper()

print(f"\n✅Registration Complete for {first_name} {last_name}!")


# User enters Phone Number
phone_number = ""
while phone_number == "":
    phone_number = input("\nPlease enter your Phone Number: ")
    if phone_number == "":
        print("⚠️ INVALID: Phone number cannot be blank.")
print(f"\n✅Thank you! The number you put is {phone_number}.")

# Ticket Count
tickets = 0
while True:
    try:
        tickets = int(input("\nHow many tickets? "))
        if tickets > 0:
            break
        print("⚠️ INVALID: Must be at least 1 ticket.")
    except ValueError:
        print("⚠️ INVALID: Please enter a NUMBER (EX. 3, not 'three').")

print(f"\n✅ Ordered {tickets} tickets.")
