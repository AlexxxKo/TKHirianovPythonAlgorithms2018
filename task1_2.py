# Нарисуйте букву S

import turtle as t

while True:
    try:
        side = int(input('Введите размер стороны буквы: '))
        break
    except ValueError:
        print('Нужно ввести число\n')

t.speed(0)

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

t.done()