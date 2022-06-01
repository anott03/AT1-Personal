import turtle, random

turtle.tracer(False)

# helper function to randomly shift the given point
def wiggle(p, degree):
    newp = list(p)
    # shift = random.randint(-1 * int(degree * 0.75), int(degree * 0.75))
    shift = random.randint(-1 * int(degree), int(degree))
    newp[0] += shift
    # shift = random.randint(-1 * int(degree * 0.75), int(degree * 0.75))
    shift = random.randint(-1 * int(degree), int(degree))
    newp[1] += shift
    return tuple(newp)

def mountain(p1_in, p2_in, p3_in, degree, t, first=True):
    if first:
        p1 = wiggle(p1_in, degree*10)
        p2 = wiggle(p2_in, degree*10)
        p3 = wiggle(p3_in, degree*10)
    else:
        p1 = p1_in
        p2 = p2_in
        p3 = p3_in
        # draws triangle
        t.up()
        t.goto(p1)
        t.down()
        t.goto(p2)
        t.goto(p3)
        t.goto(p1)

    # calculates midpoints of all sides
    mp1 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    mp2 = ((p3[0] + p2[0]) / 2, (p3[1] + p2[1]) / 2)
    mp3 = ((p1[0] + p3[0]) / 2, (p1[1] + p3[1]) / 2)
    # shifts the midpoints
    mp1 = wiggle(mp1, degree / 2 * 3)
    mp2 = wiggle(mp2, degree / 2 * 3)
    mp3 = wiggle(mp3, degree / 2 * 3)
    
    lim = 30
    # draws triangle with midpoints
    if degree > 0:
        mountain(mp1, mp2, mp3, degree - 1, t, False)
        # every possible sub-triangle
        mountain(p1, mp1, mp3, degree - 1, t,  False)
        mountain(p2, mp1, mp2, degree - 1, t,  False)
        mountain(p3, mp2, mp3, degree - 1, t, False)

t = turtle.Turtle()
t.hideturtle()
mountain((-200, -200), (200, -200), (0, 200), 5, t)
turtle.update()
turtle.mainloop()
