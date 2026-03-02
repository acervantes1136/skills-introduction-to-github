"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[ ] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[ ] 4. Task 3: Validation (isdigit check) completed.
[ ] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
Name: Amelia Cervantes
-----------------------------------------------------------------------
"""

print(f"\nTASK 1")

# --- TASK 1: TUNING THE GUITAR ---
instrument = "Acoustic Guitar"
print(len(instrument))
# Find the First and Last letter
first_letter = instrument[0]
last_letter = instrument[-1]
print(f"First letter: {first_letter}")
print(f"Last letter: {last_letter}")
# Find the ASCII character
lowest_char = min(instrument)
highest_char = max(instrument)
print(f"Original string: {instrument!r}")
print(f"Character with the minimum ASCII: {lowest_char!r}")
print(f"Character with the maximum ASCII: {highest_char!r}")

print(f"\nTASK 2")

# --- TASK 2: THE CLEANUP CREW ---
messy_input = "   vOLUME_knob_11   "
print(messy_input.strip().title())
print(messy_input.upper().strip())
print(messy_input.replace("_", " ").strip())

print(f"\nTASK 3")

# --- TASK 3: THE VALIDATOR ---
serial_number = "90210"
if serial_number.isdigit():
    print("Valid Serial")
else:
    print("Invalid Serial")

print(f"\nTASK 4")

# --- TASK 4: THE DUCK BRIDGE ---
name_string = "DUCKY"
duck_letters = list(name_string)
count = 0

print("--- Singing the Duck Song! ---")

for char in name_string:
    current_name = " ".join(duck_letters)
    print("There was a teacher who had a duck and Ducky was his Name-o")
    # Prints "Ducky" 3 times
    print((f"({current_name}) \n") * 3)
    print("and Ducky was his Name-o!\n")
    # A duck emoji will replace each letter of "Ducky"
    duck_letters[count] = "🦆"
    count += 1

# Finale (all emojis)
final_name = " ".join(duck_letters)

print("There was a teacher who had a duck and Ducky was his Name-o")
print((f"({final_name}) \n") * 3)
print("and Ducky was his Name-o!\n")
