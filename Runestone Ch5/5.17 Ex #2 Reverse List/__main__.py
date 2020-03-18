def reverse(arr):
    if len(arr) > 1:
        return [arr[len(arr)-1]] + reverse(arr[:len(arr)-1])
    else:
        return [arr[0]]
    
print(reverse([1, 2, 3]))