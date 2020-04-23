from random import randint
import timeit

# all code for sorting algorithms is from runestone
# bubble sort
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
# selection sort
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
# insertion sort
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
# shell sort
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      # print("After increments of size",sublistcount,
      #                              "The list is",alist)

      sublistcount = sublistcount // 2
# helper method for shell sort
def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

# merge sort
def mergeSort(alist):
    # print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    # print("Merging ",alist)

# quick sort
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

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


def runBubble():
    arr = [randint(0, 500) for _ in range(500)]
    bubbleSort(arr)

def runSelection():
    arr = [randint(0, 500) for _ in range(500)]
    selectionSort(arr)
    
def runInsertion():
    arr = [randint(0, 500) for _ in range(500)]
    insertionSort(arr)
    
def runShell():
    arr = [randint(0, 500) for _ in range(500)]
    shellSort(arr)
    
def runMerge():
    arr = [randint(0, 500) for _ in range(500)]
    mergeSort(arr)
    
def runQuick():
    arr = [randint(0, 500) for _ in range(500)]
    quickSort(arr)

def benchmark():
    timer = timeit.Timer("runBubble()", "from __main__ import runBubble")
    print("bubble sort: ", timer.timeit(500))

    timer = timeit.Timer("runSelection()", "from __main__ import runSelection")
    print("selection sort: ", timer.timeit(500))

    timer = timeit.Timer("runInsertion()", "from __main__ import runInsertion")
    print("insertion sort: ", timer.timeit(500))

    timer = timeit.Timer("runShell()", "from __main__ import runShell")
    print("shell sort: ", timer.timeit(500))

    timer = timeit.Timer("runMerge()", "from __main__ import runMerge")
    print("merge sort: ", timer.timeit(500))

    timer = timeit.Timer("runQuick()", "from __main__ import runQuick")
    print("quick sort: ", timer.timeit(500))


benchmark()