def bubbleSort(alist):
    up = True
    for passnum in range(len(alist)-1, 0, -1):
        if up:
            for i in range(passnum):
                if alist[i] > alist[i+1]:
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
        else:
            for i in range(passnum, 1, -1):
                if alist[i] < alist[i-1]:
                    temp = alist[i]
                    alist[i] = alist[i-1]
                    alist[i-1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
