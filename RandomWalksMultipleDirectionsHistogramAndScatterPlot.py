import matplotlib.pyplot as plt
from p5 import *
from point import Point
from field import Field
from random_walk import generate_directions, RandomWalk, keep_to_field


def nothing(a, b, c):
    pass


if __name__ == '__main__':
    plt.figure(2)
    plt.title("Scatter plot of final positions")
    plt.figure(1)
    plt.title("Distributions of random walks based on the number of directions")
    walkers = [RandomWalk() for _ in range(1000)]
    f = Field(walkers=walkers, field_height=[-50, 50], field_length=[-50, 50], rules=[nothing])
    for no_directions in [4, 5]:
        plt.figure(1)
        d = generate_directions(1, no_directions)
        print("d", d)
        directions = [Point(0, 0) for i in range(no_directions)]
        for index, value in enumerate(directions):
            value.from_polar(d[index][0], math.radians(d[index][1]))

        for walker in walkers:
            walker.reset()
            walker.set_directions(directions)

        f.walk(steps=10000)
        distances = [x.distance_from_starting_point() for x in f.walkers]
        walker_pos = f.positions()

        plt.hist(distances, bins=100, alpha=0.5, label=str(no_directions) + " directions")
        plt.figure(2)
        plt.scatter([p.x for p in walker_pos], [p.y for p in walker_pos], alpha=0.5, label=str(no_directions)
                                                                                           + " directions")

    plt.figure(1)
    plt.xlabel("Distance from starting point")
    plt.ylabel("Count")
    plt.legend(loc='upper right')

    plt.figure(2)
    plt.legend(loc='upper right')
    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()
