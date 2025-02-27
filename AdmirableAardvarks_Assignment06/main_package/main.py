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
from class_package.banana import Banana

if __name__ == "__main__":
    # Class 1: Apple created by Caitlin
    # Create an instance of the class
    sweet_apple = Apple(variety="sweet", weight="10")

    # Call the __str__ dunder method
    print(str(sweet_apple))

    # Invoke the getter properties of the class
    print(f"Sweet apple's variety is  {sweet_apple.variety}")
    print(f"Sweet apple's weight is {sweet_apple.weight}")
    print(f"Sweet apple's ripeness is {sweet_apple.is_ripe}")

    #Call the class method of ripen
    print(sweet_apple.ripen())

    # Show  the effectiveness of the method
    print(f"Sweet apple's ripeness now is {sweet_apple.is_ripe}")

    # Invoke the setter to change the properties
    sweet_apple.weight = 15
    sweet_apple.variety = "Delicious"
    sweet_apple.is_ripe = False

    # Show the effectiveness of the setter
    print(str(sweet_apple))

    # Class 2: Banana created by Asfia 
    # Create an instance of the class
    yellow_banana = Banana(variety="Yellow", size = 20)

    # Call the __str__ dunder method
    print(str(yellow_banana))

    # Invoke the getter properties of the class
    print(f"Yellow Banana's variety is {yellow_banana.variety}")
    print(f"Yellow Banana's size is {yellow_banana.size}")
    print(f"Yellow Banana's ripeness level is {yellow_banana.ripeness_level}")

    # Call the class method of ripen
    print(yellow_banana.ripen())

    # Show the effectiveness of the method
    print(f"Yellow Banana's ripeness now is {yellow_banana.ripeness_level}")

    # Invoke the setter to change the properties
    yellow_banana.variety = "Green"
    yellow_banana.size = 10
    yellow_banana.ripeness_level = 0

    # Show the effectiveness of the setter
    print(str(yellow_banana))