# File Name : orange.py
# Student Name: Leah Radcliffe
# email:  radclilr@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 2/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025 
# Brief Description of the assignment: This is out first group project in this course and we used Github 
# Brief Description of what this module does. This module instantiates objects and allows us to draw conclusions about things in different modules, This code determines how ripe a banana is on a scale of 0-10
# Citations: 

# Anything else that's relevant:

# orange.py
class Orange:
    def __init__(self, variety="Gala", weight=25, is_ripe=False):
        """Initializes an Orange object."""
        self._variety = variety
        self._weight = weight
        self._is_ripe = is_ripe

    def __str__(self):
        """Returns a string representation of the Orange."""
        return f"Orange(variety={self.variety}, weight={self.weight}g, ripe={self.is_ripe})"

    def __repr__(self):
        """Returns a detailed string representation of the Orange."""
        return f"Orange('{self.variety}', {self.weight}, {self.is_ripe})"

    @property
    def variety(self):
        """Gets the variety of the Orange."""
        return self._variety

    @variety.setter
    def variety(self, new_variety):
        """Sets the variety of the Orange."""
        if not isinstance(new_variety, str) or not new_variety.strip():
            raise ValueError("Variety must be a non-empty string.")
        self._variety = new_variety

    @property
    def weight(self):
        """Gets the weight of the Orange."""
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        """Sets the weight of the Orange."""
        if not isinstance(new_weight, (int, float)) or new_weight <= 0:
            raise ValueError("Weight must be a positive number.")
        self._weight = new_weight
    
    @property
    def is_ripe(self):
        """Gets the ripeness of the Orange."""
        return self._is_ripe
    
    @is_ripe.setter
    def is_ripe(self, new_ripe):
        """Sets the ripeness of the Orange."""
        if not isinstance(new_ripe, bool):
            raise ValueError("Is_ripe must be a boolean.")
        self._is_ripe = new_ripe

    def ripen(self):
        """Changes the Orange's ripeness and returns a message."""
        if not self.is_ripe:
            self.is_ripe = True
            return "The orange has ripened!"
        return "The orange is already ripe."