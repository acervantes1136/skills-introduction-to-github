"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. MONTHS is defined as a constant tuple ().
[ ] 3. Program uses a for loop to display each month.
[ ] 4. 'try' and 'except' blocks catch a TypeError.
[ ] 5. Comments explain why the modification failed.
-----------------------------------------------------------------------
"""

# MONTHS is defined as a constant tuple
MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)

print("\nDisplaying Months:\n" "")

# Loop will display each month
for month in MONTHS:
    print(month)

print("\nAttempting to modify the locked calendar")
print("----------------------------------------")

# Attempting to modify the first element of the tuple
try:
    MONTHS[0] = "Jan"
except TypeError as e:
    print(f"Error Caught: {e}")
    print("The systems are locked and immutable.")
    print("You cannot change, add, or remove items once they are created.")
