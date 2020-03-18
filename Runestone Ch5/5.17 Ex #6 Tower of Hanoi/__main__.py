from pythonds.basic import Stack

startPole = Stack()
intermediate = Stack()
endPole = Stack()

def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    tp.push(fp.pop())

for i in reversed(range(10)):
    startPole.push(i)

moveTower(startPole.size(), startPole, endPole, intermediate)
print(endPole.items)
