from p5 import *
from p5 import stroke_weight
from random_walk import RandomWalk, generate_directions, keep_to_field
from point import Point

no_directions = 4
d = generate_directions(20, no_directions)
diri = [Point(0,0) for i in range(no_directions)]
for index, value in enumerate(diri):
    value.from_polar(d[index][0], math.radians(d[index][1]))

r = RandomWalk(starting_point=Point(50, 50), directions=diri)

no_directions = 5
d = generate_directions(20, no_directions)
diri = [Point(0,0) for i in range(no_directions)]
for index, value in enumerate(diri):
    value.from_polar(d[index][0], math.radians(d[index][1]))

l = RandomWalk(starting_point=Point(0, 10), directions=diri)


def setup():
    background(0)
    size(1800, 900)
    stroke_weight(4)


def draw():
    keep_to_field([0,1800], [0,900], l)
    keep_to_field([0,1800], [0,900], r)

    stroke('green')
    x = r.current_point.x
    y = r.current_point.y
    r.take_steps(1)
    line(x, y, r.current_point.x, r.current_point.y)

    x = l.current_point.x
    y = l.current_point.y
    stroke("brown")
    l.take_steps(1)
    line(x, y, l.current_point.x, l.current_point.y)


if __name__ == '__main__':
    run()
