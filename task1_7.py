# Нарисуйте спираль Архимеда.

import turtle as t
from math import sin, cos, radians, pi

from lib.functions import getFloatNumber
from lib.turtle_funcs import runTurtle

@runTurtle
def main(a: float, n: float):
    # a = .05
    # end = int(n * 360)
    # for i in range(0, end + 1):
    #     x = a * i * cos(radians(i))
    #     y = a * i * sin(radians(i))
    #     t.setheading(90 + i)
    #     t.goto(x, y)
    angle = 0

    while angle < 2 * n * pi:
        r = a * angle
        x = a * r * cos(angle)
        y = a * r * sin(angle)

        angle_t = t.towards(x, y)
        t.setheading(angle_t)
        t.goto(x, y)

        angle += .1


a = getFloatNumber('Введите расстояние между витками спирали:')
n = getFloatNumber('Введите количество витков спирали (можно не целое):')

main(a, n)