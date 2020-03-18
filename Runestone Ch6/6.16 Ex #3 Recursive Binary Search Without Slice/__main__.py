import random


def recursiveBinarySearch(alist, item, first=0, last=None):
    if last is None:
        last = len(alist)-1

    if first == last:
        return False
    else:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            return recursiveBinarySearch(alist, item, first, midpoint)
        else:
            return recursiveBinarySearch(alist, item, midpoint+1, last)


def test():
    arr = range(1000)
    item = random.randrange(0, 1000)
    recursiveBinarySearch(arr, item)


def benchmark():
    import timeit
    print(timeit.timeit("test()", "from __main__ import test"))


benchmark()
