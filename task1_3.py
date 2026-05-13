# Нарисуйте квадрат

import turtle as t
from functions import getIntNumber, runTurtle

@runTurtle
def main(n):
    t.shape('turtle')
    for i in range(4):
        t.forward(n)
        t.left(90)


n = getIntNumber('Введите длину стороны квадрата:')

main(n)