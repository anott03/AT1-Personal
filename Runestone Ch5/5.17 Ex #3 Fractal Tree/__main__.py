import turtle
from turtle import *

turtle.colormode(255)

win = turtle.Screen()
# win.bgcolor(0, 0, 0)
win.title('Fractal Tree')

t = Turtle()
# t.hideturtle()
t.shape('turtle')
t.speed(0)
turtle.tracer(False)

t.left(90)
t.up()
t.goto(0, -350)
t.down()

a = 20


def tree(l):
    if l < 10:
        pass
    else:
        # makes branches brown or green depeneding on length
        if l < 15:
            t.pencolor(0, 255, 0)
        else:
            t.pencolor(128, 0, 0)

            # makes each branch a random color
        # from random import randrange
        # t.pencolor(randrange(100, 255), randrange(100, 255), randrange(100, 255))

        # t.pencolor('white')
        t.forward(l)
        t.left(a)
        turtle.update()
        tree(3 * l / 4)
        t.right(a * 2)
        turtle.update()
        tree(3 * l / 4)
        t.left(a)
        turtle.update()
        t.up()
        t.backward(l)
        t.down()
        turtle.update()


def main():
    tree(200)


main()
# keeps the window from closing after main() runs
turtle.mainloop()
