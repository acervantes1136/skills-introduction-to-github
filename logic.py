"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# Actions
red = 1
orange = 2
yellow = 3
green = 4
blue = 5
purple = 6

# Ask user to input 2 numbers
print(f"\nWe are going to create colors using the rainbow pallette!")
choice_1 = int(input("\nEnter a number 1-6: "))
choice_2 = int(input("Enter another number 1-6: "))

# User's choice will create a color
if choice_1 == 1 and choice_2 == 3:
    print(f"\nYou just created the color Orange!🍊")
elif choice_1 == 3 and choice_2 == 5:
    print(f"\nYou just created the color Green!🦖")
elif choice_1 == 1 and choice_2 == 5:
    print(f"\nYou just created the color Purple!👾")
elif (
    choice_1 == 3
    and choice_2 == 6
    or choice_1 == 5
    and choice_2 == 2
    or choice_1 == 1
    and choice_2 == 4
):
    print(f"\nEww, you just created Brown!💩")
elif not (choice_1 >= 1 and choice_1 <= 6):
    print(f"\n Invalid input. Try again!")
else:
    print(f"\nUnable to create a color with that combo. Try again!")
