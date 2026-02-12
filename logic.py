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

# Ask the User for Two Integers
while True:
    try:
        input_one = int(input("Enter the first integer: "))
        input_two = int(input("Enter the second integer: "))
        break
    except ValueError:
        print("Invalid input. Please enter integers only!")

print("\nLogical Checks Results")

# Performing 6 Logical Checks
both_positive = input_one > 0 and input_two > 0
print(f"Are both integers greater than 0? {both_positive}")
both_greater_than_100 = input_one > 100 and input_two > 100
print(f"Are both integers greater than 100? {both_greater_than_100}")
either_even = input_one % 2 == 0 or input_two % 2 == 0
print(f"Is either integer even? {either_even}")
either_less_than_100 = input_one < 100 or input_two < 100
print(f"Is either integer less than 100? {either_less_than_100}")
not_equal = input_one != input_two
print(f"Are the integers not equal? {not_equal}")
not_zero = input_one != 0 and input_two != 0
print(f"Are both integers not zero? {not_zero}")

# Using if/elif/else
print(f"\nCategorize the first integer: ")

if input_one > 0:
    print(f"{input_one} is a Positive number.")
elif input_one < 0:
    print(f"{input_one} is a Negative number.")
else:
    print(f"{input_one} is Zero.")

print(f"\nCategorize the second integer: ")

if input_two > 0:
    print(f"{input_two} is a Positive number.")
elif input_two < 0:
    print(f"{input_two} is a Negative number.")
else:
    print(f"{input_two} is Zero.")
