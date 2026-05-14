# Нарисуйте n вложенных квадратов с шагом step.

import turtle as t

from lib.functions import getIntNumber
from lib.turtle_funcs import runTurtle, draw_square

@runTurtle
def main(n, step):
    t.shape('turtle')
    side = 10;
    for i in range(n):
        draw_square(side)
        t.penup()
        t.backward(step)
        t.right(90)
        t.forward(step)
        t.left(90)
        t.pendown()
        side += 2 * step

n = getIntNumber('Введите количество квадратов:')
step = getIntNumber('Введите расстояние между квадратами:')

main(n, step)