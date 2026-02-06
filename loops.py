"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# Step 1:
destination = True

while destination:
    print("\nMom! Are we there yet?")

    # User responds as parent
    answer = input("Your response (yes/no): ")
    if answer == "yes":
        destination = False

# Step 2:
print("\n\n\nMom: Let's count down to pass time!")

for i in range(99, 0, -1):
    print(
        f"\n{i} Bottles of Beer on the wall!\n{i} Bottles of Beer!\nTake one down and pass it around..."
    )
print("\nNo more Bottles of Beer on the wall!")
