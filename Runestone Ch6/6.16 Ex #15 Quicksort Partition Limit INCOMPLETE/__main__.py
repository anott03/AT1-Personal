def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:

        splitpoint = partition(alist, first, last)

        if splitpoint - 1 - first > 3:
            quickSortHelper(alist, first, splitpoint - 1)
        else:
            tmp = alist[first:splitpoint - 1]
            insertionSort(tmp)
            alist[first:splitpoint - 1] = tmp

        if last - (splitpoint + 1) > 3:
            quickSortHelper(alist, splitpoint + 1, last)
        else:
            tmp = alist[splitpoint + 1:last]
            insertionSort(tmp)
            alist[splitpoint + 1:last] = tmp


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


def insertionSort(alist, first=0, last=-1):
    if last == -1:
        last = len(alist)

    for index in range(first+1, last):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue


alist = []

import random
for i in range(0, 50):
    alist.append(random.randint(0, 500))

# bug where the second item is not always sorted
# ex in [54,26,93,17,77,31,44,55,20] 26 does not get sorted

# alist = [54,26,93,17,77,31,44,55,20]

quickSort(alist)
print(alist)
