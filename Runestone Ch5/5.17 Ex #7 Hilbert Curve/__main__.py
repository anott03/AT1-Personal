import turtle

'''
    A → − B F + A F A + F B −
    B → + A F − B F B − F A +
    
    F is draw forward
    - is turn left 90 degrees
    + is turn right 90 degrees
    
    from: https://en.wikipedia.org/wiki/Hilbert_curve
'''


def hilbert(length, rule, degree, t):
    if degree > 0:
        if rule == 'A':
            t.left(90)
            hilbert(length, 'B', degree-1, t)
            t.forward(length)
            t.right(90)
            hilbert(length, 'A', degree-1, t)
            t.forward(length)
            hilbert(length, 'A', degree - 1, t)
            t.right(90)
            t.forward(length)
            hilbert(length, 'B', degree-1, t)
            t.left(90)
        if rule == 'B':
            t.right(90)
            hilbert(length, 'A', degree - 1, t)
            t.forward(length)
            t.left(90)
            hilbert(length, 'B', degree - 1, t)
            t.forward(length)
            hilbert(length, 'B', degree - 1, t)
            t.left(90)
            t.forward(length)
            hilbert(length, 'A', degree - 1, t)
            t.right(90)

t = turtle.Turtle()
t.hideturtle()
turtle.tracer(False)

hilbert(20, 'A', 4, t)

turtle.update()
turtle.mainloop()