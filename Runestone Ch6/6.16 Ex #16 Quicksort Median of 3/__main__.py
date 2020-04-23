def quickSortMed3(alist):
    quickSortHelperMed3(alist, 0, len(alist) - 1)


def quickSortHelperMed3(alist, first, last):
    if first < last:
        splitpoint = partitionMed3(alist, first, last)

        quickSortHelperMed3(alist, first, splitpoint - 1)
        quickSortHelperMed3(alist, splitpoint + 1, last)


# helper to find the median of first, last, and middle items
def findMedian(alist, first, last):
    x = alist[first]
    y = alist[(first + last) // 2]
    z = alist[last]

    if y < x < z:
        return x
    elif z < x < y:
        return x
    elif z < y < x:
        return y
    elif x < y < z:
        return y
    elif y < z < x:
        return z
    else:
        return z


def partitionMed3(alist, first, last):
    pivotvalue = findMedian(alist, first, last)

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


from random import randint
import timeit

def testNormal():
    arr = []
    for i in range(500):
        arr.append(randint(0, 500))

    quickSort(arr)


def testMed3():
    arr = []
    for i in range(500):
        arr.append(randint(0, 500))

    quickSortMed3(arr)

normal_timer = timeit.Timer("testNormal()", "from __main__ import testNormal")
med3_timer = timeit.Timer("testMed3()", "from __main__ import testMed3")
print("normal: " + str(normal_timer.timeit(1000)))
print("med3: " + str(med3_timer.timeit(1000)))
