# Нарисуйте n вложенных квадратов с шагом step.

import turtle as t
from functions import getIntNumber, runTurtle

@runTurtle
def main(n, step):
    t.shape('turtle')
    side = 10;
    for i in range(n):
        for _ in range(4):
            t.forward(side)
            t.left(90)
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