# File Name : AdmirableArdvards_Assignment06
# Student Name: Caitlin Hutchins
# email: hutchicu@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:  2/26/25
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This is out first group project in this course and we used Github.

# Brief Description of what this module does: This module instantiates objects
# Citations: 
# Anything else that's relevant:

# apple.py
class Apple:
    def __init__(self, variety="Gala", weight=100, is_ripe=False):
        """Initializes an Apple object."""
        self._variety = variety
        self._weight = weight
        self._is_ripe = is_ripe

    def __str__(self):
        """Returns a string representation of the Apple."""
        return f"Apple(variety={self.variety}, weight={self.weight}g, ripe={self.is_ripe})"

    def __repr__(self):
        """Returns a detailed string representation of the Apple."""
        return f"Apple('{self.variety}', {self.weight}, {self.is_ripe})"

    @property
    def variety(self):
        """Gets the variety of the Apple."""
        return self._variety

    @variety.setter
    def variety(self, new_variety):
        """Sets the variety of the Apple."""
        if not isinstance(new_variety, str) or not new_variety.strip():
            raise ValueError("Variety must be a non-empty string.")
        self._variety = new_variety

    @property
    def weight(self):
        """Gets the weight of the Apple."""
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        """Sets the weight of the Apple."""
        if not isinstance(new_weight, (int, float)) or new_weight <= 0:
            raise ValueError("Weight must be a positive number.")
        self._weight = new_weight
    
    @property
    def is_ripe(self):
        """Gets the ripeness of the Apple."""
        return self._is_ripe
    
    @is_ripe.setter
    def is_ripe(self, new_ripe):
        """Sets the ripeness of the Apple."""
        if not isinstance(new_ripe, bool):
            raise ValueError("Is_ripe must be a boolean.")
        self._is_ripe = new_ripe

    def ripen(self):
        """Changes the Apple's ripeness and returns a message."""
        if not self.is_ripe:
            self.is_ripe = True
            return "The apple has ripened!"
        return "The apple is already ripe."