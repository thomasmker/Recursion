def binary_search(arr, left, right, x):
    if left > right:
        return -1
    
    mid = int((left + right) / 2)

    if x == arr[mid]:
        return mid
    
    if x < arr[mid]:
        return binary_search(arr, left, mid - 1, x)
     
    return binary_search(arr, mid + 1, right, x)

arr = [-1, 0, 1, 2, 3, 4, 7, 9, 10, 20]

print(binary_search(arr, 0, len(arr) - 1, 10))