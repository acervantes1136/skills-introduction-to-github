"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""

import random

# Tuple of at least 8 responses
RESPONSES = (
    "Yes, definitely!",
    "No way.",
    "Maybe...",
    "Ask again later.",
    "Most likely.",
    "Very doubtful.",
    "Outlook not so good.",
    "Better not tell you now...",
)

print("Welcome to the Digital Oracle!")
print("Ask a question and receive an answer... (type 'quit' to exit)\n")

while True:
    question = input("What is your question? ")

    # Check if user wants to quit
    if "quit" in question.lower():
        print(f"\nThank you for using the Digital Oracle! Goodbye👋")
        break

    # Choose a response randomly
    answer = random.choice(RESPONSES)
    print("🔮", answer, "\n")
