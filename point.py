import math
import numbers


class Point:
    """class for modelling a point"""

    def __init__(self, x=0., y=0., ):
        if isinstance(x, numbers.Number) is False or isinstance(y, numbers.Number) is False:
            raise ValueError("Arguments must be numeric")
        self.x = x
        self.y = y

        self.distance_method = {"euclid": lambda self, other_point: math.sqrt(
            (self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2),
                                "manhattan": lambda self, other_point: abs(self.x - other_point.x) + abs(
                                    self.y - other_point.y),
                                "minkowski": lambda self, other_point, p: (abs(self.x - other_point.x)**p +
                                                                          abs(self.y-other_point.y)**p)**(1/p)
        }
        self.distance_method_selected = "euclid"

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y)

    def __add__(self, other_point):
        r = Point()
        r.x = self.x + other_point.x
        r.y = self.y + other_point.y
        return r

    def from_polar(self, r, t):
        self.x = r*math.cos(t)
        self.y = r*math.sin(t)

    def add_distance_method(self, name, function):
        self.distance_method[name] = function

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

