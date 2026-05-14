# Нарисуйте букву S

import turtle as t

from lib.functions import getIntNumber
from lib.turtle_funcs import runTurtle

@runTurtle
def main(side):
    t.shape('turtle')
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.right(90)
    t.forward(side)
    t.right(90)
    t.forward(side)

side = getIntNumber('Введите ширину буквы:')

main(side)