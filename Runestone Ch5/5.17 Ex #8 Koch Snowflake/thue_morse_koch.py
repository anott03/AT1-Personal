import turtle
import thueMorse

# def thueMorse():
#     # initialize
#     tms = '0'
#     curr = 0
#     while True:
#         # generate next sequence
#         if curr == len(tms):
#             tmp = ''
#             for i in range(len(tms)):
#                 if tms[i] is '0':
#                     tmp += '1'
#                 else:
#                     tmp += '0'
#             tms += tmp
#         yield tms[curr]
#         curr += 1

# def koch(length, degree, t):
#     thue_morse_val = thueMorse()
#     while True:
#         a = next(thue_morse_val)
#         if a == '0':
#             t.forward(length)
#         elif a == '1':
#             t.left(60)

def negate(token):
    if token == '0':
        return '1'
    return '0'


def thueMorse(degree, prev='0'):
    if degree > 0:
        seq = prev
        for char in prev:
            seq += negate(char)
        thueMorse(degree-1, seq)
    else:
        return prev

def koch(degree, t):
    for char in thueMorse(degree):
        if char == '0':
            t.forward(4)
        else:
            t.left(60)

t = turtle.Turtle()
t.speed('fastest')
koch(10, t)
turtle.mainloop()