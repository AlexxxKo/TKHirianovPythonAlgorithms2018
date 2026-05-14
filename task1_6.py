# Нарисуйте паука с n лапами

import turtle as t

from lib.functions import getIntNumber
from lib.turtle_funcs import runTurtle, draw_line_with_stamp


@runTurtle
def main(n, side):
    t.shape('turtle')
    angle = 360 / n
    for i in range(n):
        draw_line_with_stamp(side)
        t.right(angle)
    t.stamp()

n = getIntNumber('Введите количество ног у паука:')
side = getIntNumber('Введите размер ног паука:')

main(n, side)