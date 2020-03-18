from pythonds.basic import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if len(token) > 1:
            raise RuntimeWarning("Token length greater than 1 character")

        if token in "0123456789":
            operandStack.push(int(token))
        elif token in "+-*/":
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
        else:
            raise RuntimeError("Invalid token")
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


print(postfixEval('7 8 + 3 2 + /'))
