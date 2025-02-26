# File Name : main.py
# Student Name: Nathan Sharpe
# email: sharpenn@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 2/27/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Collaborate with a group to add classes to a project and instantiate them and demonstrate
# their functionality within main.

# Brief Description of what this module does. Introduces us to OOP in python including classes, properties and methods.
# Citations: In class work from 2/20/25 "VehicleClass"

# Anything else that's relevant: I (Nathan Sharpe) handled main while Caitlin, Leah and Asfia created classes.
from class_package.apple import Apple

if __name__ == "__main__":
    # Class 1: Apple created by Caitlin
    # Create an instance of the class
    sweet_apple = Apple(variety="sweet", weight="10")

    # Call the __str__ dunder method
    print(str(sweet_apple))

    # Demonstrate the properties of the object with the getter
    print(f"Apple's variety is  {sweet_apple.variety}")
    print(f"Apple's weight is {sweet_apple.weight}")
    print(f"Apple's ripeness is {sweet_apple.is_ripe}")

    #Call the class method of ripen
    print(sweet_apple.ripen())

    # Show methods effectiveness
    print(f"Apple's ripeness now is {sweet_apple.is_ripe}")

    # Invoke the setter to change the properties
    sweet_apple.weight = 10
    sweet_apple.variety = "Delicious"

    # Show effectiveness of the setter
    print(str(sweet_apple))