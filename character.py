import random


class Character:
    """ this is the Parent class for Hero and Monster. with complex getters and setters. """

    def __init__(self):
        # Rolling the dice to initialize combat strength between 1 and 6 and health points between 1 and 20
        self.__combat_strength = random.randint(1, 6)
        self.__health_points = random.randint(1, 20)

    @property
    def combat_strength(self):
        # Complex getter for the private __combat_strength.

        return self.__combat_strength

    @combat_strength.setter
    def combat_strength(self, new_strength):

        # Complex setter for the private __combat_strength. this will also ensure the value is an integer >= 0.

        if isinstance(new_strength, int) and new_strength >= 0:
            self.__combat_strength = new_strength
        else:
            raise ValueError("Combat strength must be a non-negative integer.")

    @property
    def health_points(self):
        # Complex getter for the private __health_points.
        return self.__health_points

    @health_points.setter
    def health_points(self, new_hp):

        # Complex setter for the private __health_points.
        # like (private __combat_strength) it will also ensure it's an integer >= 0.

        if isinstance(new_hp, int) and new_hp >= 0:
            self.__health_points = new_hp
        else:
            raise ValueError("Health points must be a non-negative integer.")

    def __del__(self):

        # this is thge Parent destructor which will be extended in child classes.
        pass
