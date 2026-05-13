# Нарисуйте букву S

import turtle as t
from functions import getIntNumber, runTurtle

side = getIntNumber('Введите ширину буквы')

def func() -> None:
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

runTurtle(func)