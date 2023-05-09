def quickSort(arr,l,r):
    if l < r:
        s=lomuto(arr, l, r)
        quickSort(arr, l, s-1)
        quickSort(arr, s + 1, r)
        return arr

def lomuto(arr, l, r):
    p = arr[r]
    s = l
    for i in range(l,r):
        if arr[i] <= p :
            arr[i], arr[s] = arr[s], arr[i]
            s += 1
    arr[s], arr[r] = arr[r], arr[s]
    return s

arr = [8,6,9,4,5,1,2,3,0,7]

print(quickSort(arr,0, len(arr) - 1))