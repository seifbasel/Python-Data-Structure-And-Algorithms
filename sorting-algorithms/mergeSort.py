def mergeSort(arr):
    # Check if the array has more than one element
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        l = arr[:mid]  # Divide the array into two halves
        r = arr[mid:]
        
        mergeSort(l)  # Recursively sort the left half
        mergeSort(r)  # Recursively sort the right half
        merge(l, r, arr)  # Merge the sorted halves

def merge(l, r, arr):
    i = j = k = 0

    # Merge the two sorted arrays
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    # Check for any remaining elements in the left array
    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1

    # Check for any remaining elements in the right array
    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1

# Example usage
arr = [5, 2, 1, 4, 9, 8, 22, 3, 7, 16]
mergeSort(arr)
print("Sorted Array:", arr)
