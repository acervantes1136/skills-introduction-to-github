"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""


def manage_seating():

    # 20 seat option
    seats = [i for i in range(1, 21)]

    # Repeats until user quits (0 = exit)
    while len(seats) > 0:
        # Displays list of available seats
        print(f"\nAvailable seats: {seats}")
        # User picks seat
        try:
            choice = int(input("Enter seat number to book (0 to exit): "))
        except ValueError:
            print("Invalid input: Please enter a number!")
            continue
        if choice == 0:
            print("Exiting site")
            break
        if choice in seats:
            # Removes seat
            seats.remove(choice)
            print(f"Seat {choice} booked successfully.")
        else:
            print(
                "Invalid input: Seat does not exist or already taken. Try again Please!"
            )

    # Checks for final seat
    if len(seats) == 0:
        print("\nSorry, all seats are booked! Have a good day :)")


manage_seating()
