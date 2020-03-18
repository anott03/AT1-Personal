import time
from random import randrange


def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint + 1

    return found


def recursiveBinarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            return recursiveBinarySearch(alist[:midpoint], item)
        else:
            return recursiveBinarySearch(alist[midpoint+1:], item)


def testSequential():
    arr = range(1000)
    item = randrange(0, 1000)
    binarySearch(arr, item)


def testRecursive():
    arr = range(1000)
    item = randrange(0, 1000)
    recursiveBinarySearch(arr, item)


def benchmark():
    import timeit
    print(timeit.timeit("testSequential()", "from __main__ import testSequential"))
    print(timeit.timeit("testRecursive()", "from __main__ import testRecursive"))


benchmark()
