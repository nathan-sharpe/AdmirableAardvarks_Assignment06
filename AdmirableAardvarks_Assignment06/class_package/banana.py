# File Name : AdmirableArdvards_Assignment06
# Student Name: Asfia Siddiqui
# email: siddiqaf@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:  2/26/25
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This is out first group project in this course and we used Github.

# Brief Description of what this module does: This code determines how ripe a banana is on a scale of 0-10
# Citations: 
# Anything else that's relevant:


# banana.py
class Banana:
    def __init__(self, variety="Cavendish", size=15, ripeness_level=0):
        """
        Initializes a Banana object.
        """
        self._variety = variety
        self._size = size  # Size in cm
        self._ripeness_level = ripeness_level  # 0 = unripe, 10 = fully ripe

    def __str__(self):
        """
        Returns a string representation of the Banana.
        """
        ripeness_status = "Unripe" if self.ripeness_level < 5 else "Ripe"
        return f"{self.variety} Banana ({self.size}cm, {ripeness_status})"

    def __repr__(self):
        """
        Returns a detailed representation of the Banana.
        """
        return f"Banana(variety='{self.variety}', size={self.size}, ripeness_level={self.ripeness_level})"

    @property
    def variety(self):
        """
        Gets the variety of the Banana.
        """
        return self._variety

    @variety.setter
    def variety(self, new_variety):
        """
        Sets the variety of the Banana.
        """
        if not isinstance(new_variety, str) or not new_variety.strip():
            raise ValueError("Variety must be a non-empty string.")
        self._variety = new_variety

    @property
    def size(self):
        """
        Gets the size of the Banana.
        """
        return self._size

    @size.setter
    def size(self, new_size):
        """
        Sets the size of the Banana.
        """
        if not isinstance(new_size, (int, float)) or new_size <= 0:
            raise ValueError("Size must be a positive number.")
        self._size = new_size

    @property
    def ripeness_level(self):
        """
        Gets the ripeness level of the Banana.
        """
        return self._ripeness_level

    @ripeness_level.setter
    def ripeness_level(self, new_level):
        """
        Sets the ripeness level of the Banana.
        """
        if not isinstance(new_level, int) or not (0 <= new_level <= 10):
            raise ValueError("Ripeness level must be an integer between 0 and 10.")
        self._ripeness_level = new_level

    def ripen(self):
        """
        Increases the ripeness level of the Banana.
        """
        if self.ripeness_level < 10:
            self.ripeness_level += 3  # Speeds up ripening
            return "The banana is ripening!"
        return "The banana is already fully ripe."