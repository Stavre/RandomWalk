import math
import random
import numbers
import secrets
import statistics
import numpy.random

class Point:
    """class for modelling a point"""

    def __init__(self, x=0., y=0.):
        if isinstance(x, numbers.Number) is False or isinstance(y, numbers.Number) is False:
            raise ValueError("Arguments must be numeric")
        self.x = x
        self.y = y

        self.distance_method = {"euclid": lambda self, other_point: math.sqrt(
            (self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2),
                                "manhattan": lambda self, other_point: abs(self.x - other_point.x) + abs(
                                    self.y - other_point.y)}
        self.distance_method_selected = "euclid"

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y)

    def __add__(self, other_point):
        r = Point()
        r.x = self.x + other_point.x
        r.y = self.y + other_point.y
        return r

    def get_distance_method(self):
        return self.distance_method_selected

    def get_distance_methods(self):
        return self.distance_method

    def set_distance_method(self, method):
        if method in self.distance_method:
            self.distance_method_selected = method
        else:
            raise ValueError("No such distance method exists")

    def distance(self, other_point):
        return self.distance_method[self.distance_method_selected](self, other_point)


class RandomWalk:
    """class for simulating random walks"""

    def __init__(self, starting_point=Point(0.0, 0.0),
                 directions=[Point(0.0, 1.0), Point(0.0, -1.0), Point(1.0, 0.0), Point(-1.0, 0.0)]):
        """init random walk with (x, y) = (0, 0) as starting point
        and directions as [(0, 1) north, (0, -1) south, (1, 0) east, (-1, 0) west]"""
        if isinstance(starting_point, Point) is False:
            raise ValueError("Starting point must be of Point type")
        if all(isinstance(t, Point) for t in directions) is False:
            raise ValueError("All directions must be of Point type")

        self.starting_point = starting_point
        self.current_point = starting_point
        self.directions = directions
        self.random_method = random.choice

    def set_random_method(self, met):
        self.random_method = met

    def __take_step(self):
        """private method for taking a step in a random direction"""
        self.current_point = self.current_point + self.random_method(self.directions)

    def take_steps(self, steps):
        """simulates taking multiple steps"""
        for _ in range(steps):
            self.__take_step()

    def distance_from_starting_point(self):
        """returns distance from starting point to current position"""
        return self.starting_point.distance(self.current_point)

    def reset(self):
        """sets the current position to the starting position"""
        self.current_point = self.starting_point

    def set_distance_method(self, method):
        self.current_point.set_distance_method(method)
        self.current_point.set_distance_method(method)

    def walk(self, number_of_steps):
        for i in range(number_of_steps):
            self.__take_step()

        return self.distance_from_starting_point()


if __name__ == '__main__':
    w = RandomWalk()

