def quickSort(arr, l, r):
    if l < r:
        s = hoare(arr, l, r)
        quickSort(arr, l, s)
        quickSort(arr, s + 1, r)
        return arr

def hoare(arr, l, r):
    p = arr[l]
    i = l - 1
    j = r + 1
    while True:
        i += 1
        while arr[i] < p:
            i += 1
        j -= 1
        while arr[j] > p:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


arr = [8, 6, 7, 5, 4, 3, 9, 1, 2]
print(quickSort(arr, 0, len(arr)-1))
