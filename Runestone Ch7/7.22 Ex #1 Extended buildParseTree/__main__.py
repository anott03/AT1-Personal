from pythonds.basic import Stack
from pythonds.trees import BinaryTree

def buildParseTree(fpexp):
    fplist = []

    while len(fpexp) != 0:
        ch = fpexp[0]
        if ch in '()+-*/':
            fplist.append(ch)
            fpexp = fpexp[1:]
        else:
            i = 0
            while fpexp[i] not in '()+-*/':
                i += 1
            fplist.append(fpexp[:i])
            fpexp = fpexp[i:]

    print(fplist)

    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree

# pt = buildParseTree("( ( 10 + 5 ) * 3 )")
pt = buildParseTree("((10+5)*3)")
pt.postorder()
