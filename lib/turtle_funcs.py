import turtle as t

def draw_line_with_stamp(side):
    t.forward(side)
    t.stamp()
    t.backward(side)


def draw_square(side):
    for _ in range(4):
        t.forward(side)
        t.left(90)


def runTurtle(func):
    def wrapper(*args, **kwargs):
        t.speed(0)
        func(*args, **kwargs)
        t.hideturtle()
        t.done()
    return wrapper