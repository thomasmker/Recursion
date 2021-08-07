def merge_sort(data, start, end):
    if start < end:
        mid = int(start + end / 2)
        merge_sort(data, start, mid)
        merge_sort(data, mid + 1, end)
        merge(data, start, mid, end)

def merge(data, start, mid, end):
    # build temp array to avoid modifying the original data
    temp = [None] * (end - start + 1)
    i = start
    j = mid +1
    k = 0
    # while both sub-arrays have values, then try and merge them in sorted order
    while i <= mid and j <= end:
        if data[i] <= data[j]:
            temp[k] = data[i]
            i += 1
        else:
            temp[k] = data[j]
            j += 1
        k += 1

    # Add the rest of the values from the left sub-array into the result
    while i <= mid:
        temp[k] = data[i]
        i += 1
        k += 1

    # Add the rest of the values from the right sub-array into the result
    while j <= end:
        temp[k] = data[j]
        j += 1
        k += 1

    i = start
    while i <= end:
        data[i] = temp[i - start]
        i += 1

data = [3, 2, -1]
merge_sort(data, 0, len(data) - 1)
print(data)