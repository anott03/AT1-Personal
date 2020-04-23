from pythonds.basic import Stack

def infixEval(exp):
    operators = Stack()
    operands = Stack()
    tokens = exp.split()

    for token in tokens:
        if token.isdigit():
            operands.push(int(token))
        elif token in "+-*/":
            operators.push(token)
        else:
            raise RuntimeError("Invalid Token " + token)

    while operators.size() != 0:
        operator = operators.pop()
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

def calculator():
    cmd = input("What would you like to do?\n1. Calculate\n2. Exit\n")
    if int(cmd.strip()) == 1:
        expression = input("Enter an infix expression: ")
        print(infixEval(expression))
        calculator()
    elif int(cmd.strip()) == 2:
        quit()
    else:
        print("Invalid Command")

calculator()