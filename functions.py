import turtle as t

def getIntNumber(question: str) -> int:
    while True:
        try:
            n = int(input(f'{question} '))
            break
        except ValueError:
            print('Нужно ввести целое число\n')

    return n

def getFloatNumber(question: str) -> int:
    while True:
        try:
            n = float(input(f'{question}: '))
            break
        except ValueError:
            print('Нужно ввести число\n')

    return n

def runTurtle(func):
    def wrapper(*args, **kwargs):
        t.speed(0)
        func(*args, **kwargs)
        t.hideturtle()
        t.done()
    return wrapper