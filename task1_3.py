# Нарисуйте квадрат

import turtle as t

from lib.functions import getIntNumber
from lib.turtle_funcs import runTurtle

@runTurtle
def main(n):
    t.shape('turtle')
    for i in range(4):
        t.forward(n)
        t.left(90)


n = getIntNumber('Введите длину стороны квадрата:')

main(n)