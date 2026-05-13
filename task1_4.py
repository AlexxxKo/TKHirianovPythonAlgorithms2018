# Нарисуйте окружность, не используя circle()

import turtle as t
from functions import getFloatNumber, runTurtle
from math import pi

@runTurtle
def main(r):
    l = 2 * pi * r
    n = 100
    angle = 360 / n
    side = l / n

    t.shape('turtle')
    t.left(90)
    for i in range(n):
        t.forward(side)
        t.left(angle)


r = getFloatNumber('Введите радиус окружности:')

main(r)
