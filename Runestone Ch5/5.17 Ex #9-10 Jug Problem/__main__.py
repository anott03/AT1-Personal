
def jug(goal=2, a=4, b=3, aJug=0, bJug=0):
    if aJug == 0:
        aJug = a

    prevb = bJug

    bJug += aJug
    if bJug > b:
        bJug = b

    aJug = a - (b - prevb)

    if bJug == b:
        bJug = 0

    if aJug != goal:
        return jug(goal, a, b, aJug, bJug)
    else:
        return aJug


print(jug())
