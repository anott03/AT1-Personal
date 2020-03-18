from pythonds.basic import Stack

def infixEval(exp):
    opStack = Stack()
    operands = Stack()
    tokens = exp.split()
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    postfixList = []
    for token in tokens:

        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        elif token in "+-*/":
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)
        else:
            raise RuntimeError("Invalid Token")


        if token.isdigit():
            operands.push(int(token))
        elif token in "+-*/":
            opStack.push(token)
        else:
            raise RuntimeError("Invalid Token " + token)

    while opStack.size() != 0:
        operator = opStack.pop()
        operand2 = operands.pop()
        operand1 = operands.pop()
        operands.push(doMath(operator, operand1, operand2))

    return operands.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(infixEval("26 * 2 + 3"))