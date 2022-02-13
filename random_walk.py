import random
from point import Point


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

    def set_directions(self, directions):
        if all(isinstance(t, Point) for t in directions) is False:
            raise ValueError("All directions must be of Point type")
        self.directions = directions

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
        self.starting_point.set_distance_method(method)
        self.current_point.set_distance_method(method)

    def walk(self, number_of_steps):
        """simulates taking  steps"""
        if number_of_steps < 0:
            raise ValueError("Number of steps < 0 not allowed")
        for i in range(number_of_steps):
            self.__take_step()

        return self.distance_from_starting_point()

def keep_to_field(length, heigth, RandomWalk):
    if RandomWalk.current_point.x > length[1]:
        RandomWalk.current_point.x = length[0]
    if RandomWalk.current_point.x < length[0]:
        RandomWalk.current_point.x = length[1]

    if RandomWalk.current_point.y > heigth[1]:
        RandomWalk.current_point.y = heigth[0]
    if RandomWalk.current_point.y < heigth[0]:
        RandomWalk.current_point.y = heigth[1]

def generate_directions(r, n):
    increment = 360 / n
    current_angle = increment
    d = []
    while current_angle <= 360.1:
        d.append([r, current_angle])
        current_angle = current_angle + increment
    print(d)
    return d
