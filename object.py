"""
-----------------------------------------------------------------------
ASSIGNMENT 14A: Object practice
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a class for a part of your project using PascalCase.
[ ] 3. Use __init__ to set private attributes (__variable).
[ ] 4. Write Setters and Getters for the attributes.
[ ] 5. Write a summary function that returns a formatted description.
[ ] 6. Instantiate two distinct objects and print their summaries.
-----------------------------------------------------------------------
"""


class Car:
    def __init__(self, make, model, year, mileage):
        # Private attributes & listing different variables
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = mileage

    """Ensures the information inputted matches the attributes"""

    # Setters
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        if year > 1885:  # The first car invented around 1886 so nothing before that
            self.__year = year
        else:
            print("Invalid year.")

    def set_mileage(self, mileage):
        if mileage >= 0:
            self.__mileage = mileage
        else:
            print("ERROR: Mileage cannot be negative.")

    # Getters
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage

    # Summary method
    def summary(self):
        return (
            f"{self.__year} {self.__make} {self.__model} with {self.__mileage} miles."
        )

    """Ensures that the information below is in the correct
    spot to print out the summary"""


# Instantiate two objects
car1 = Car("Toyota", "Camry", 2020, 25000)
car2 = Car("Honda", "Civic", 2018, 40000)

# Print summaries
print(car1.summary())
print(car2.summary())
"""This prints out the summary
this is what the user sees as the final project"""
