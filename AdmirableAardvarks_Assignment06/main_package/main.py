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
    # Create an Apple object
    my_apple = Apple(variety="Honeycrisp", weight=5)

    # Demonstrate the __str__ dunder method
    print("Using __str__:", str(my_apple))

    # Show initial state
    print("\nInitial Apple state:")
    print(f"Variety: {my_apple.variety}")
    print(f"Weight: {my_apple.weight}")
    print(f"Is ripe: {my_apple.is_ripe}")

    # Use the ripen method
    print("\nRipening the apple...")
    print(my_apple.ripen())

    # Show updated state
    print("\nApple state after ripening:")
    print(f"Is ripe: {my_apple.is_ripe}")

    # Change apple attributes
    my_apple.variety = "Sweer"
    my_apple.weight = 8

    # Display final state
    print("\nFinal Apple state:")
    print(str(my_apple))