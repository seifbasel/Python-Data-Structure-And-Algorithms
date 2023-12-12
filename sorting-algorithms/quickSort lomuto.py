def quickSort(arr, l, r):
    # Check if there is more than one element in the subarray
    if l < r:
        # Partition the array using Lomuto scheme and get the partition index
        partition_index = lomuto(arr, l, r)
        
        # Recursively apply quickSort to the left and right subarrays
        quickSort(arr, l, partition_index - 1)
        quickSort(arr, partition_index + 1, r)
        
        return arr

def lomuto(arr, l, r):
    # Choose the pivot element (last element in the subarray)
    pivot = arr[r]
    
    # Initialize the partition index
    s = l
    
    # Iterate through the subarray and rearrange elements based on the pivot
    for i in range(l, r):
        if arr[i] <= pivot:
            # Swap arr[i] and arr[s]
            arr[i], arr[s] = arr[s], arr[i]
            s += 1

    # Swap arr[s] and arr[r] to place the pivot in its final position
    arr[s], arr[r] = arr[r], arr[s]
    
    return s

# Example usage
arr = [8, 6, 9, 4, 5, 1, 2, 3, 0, 7]
print("Original Array:", arr)
print("Sorted Array:", quickSort(arr, 0, len(arr) - 1))
