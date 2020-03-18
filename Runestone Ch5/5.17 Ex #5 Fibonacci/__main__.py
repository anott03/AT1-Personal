def fibonacci(degree):
    if degree > 1:
        return fibonacci(degree - 1) + fibonacci(degree-2)
    else:
        return 1

print(fibonacci(4))