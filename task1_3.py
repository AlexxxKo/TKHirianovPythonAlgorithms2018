# Нарисуйте квадрат

import turtle as t
from functions import getIntNumber, runTurtle

def func():
    n = getIntNumber('Введите длину стороны квадрата')

    t.shape('turtle')
    for i in range(4):
        t.forward(n)
        t.left(90)

runTurtle(func)