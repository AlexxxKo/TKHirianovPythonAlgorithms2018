# Нарисуйте спираль Архимеда.

import turtle as t
from math import sin, cos, radians

from lib.functions import getFloatNumber
from lib.turtle_funcs import runTurtle

@runTurtle
def main(n: float):
    a = .05
    end = int(n * 360)
    for i in range(0, end + 1):
        x = a * i * cos(radians(i))
        y = a * i * sin(radians(i))
        t.setheading(90 + i)
        t.goto(x, y)

n = getFloatNumber('Введите количество витков спирали (можно не целое):')

main(n)