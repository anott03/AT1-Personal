# this works but is not more efficient than merge sort using slice
def mergeSort(alist):
    if len(alist) <= 1:
        return alist

    middle = len(alist) // 2
    left = []
    right = []
    for i in range(middle):
        left.append(alist[i])

    for j in range(middle, len(alist)):
        right.append(alist[j])

    left = mergeSort(left)
    right = mergeSort(right)

    if left[len(left)-1] <= right[0]:
        left += right
        return left

    result = merge(left, right)
    return result

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    result += left
    result += right
    return result

alist = [54,26,93,17,77,31,44,55,20]
alist = mergeSort(alist)
print(alist)
