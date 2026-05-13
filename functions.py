import turtle as t


def getIntNumber(question: str) -> int:
    while True:
        try:
            n = int(input(f'{question}: '))
            break
        except ValueError:
            print('Нужно ввести число\n')

    return n

def runTurtle(func) -> None:
    t.speed(0)
    func()
    t.done()