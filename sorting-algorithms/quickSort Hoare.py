def quickSort(arr, l, r):
    # Check if there is more than one element in the subarray
    if l < r:
        # Partition the array and get the partition index
        partition_index = hoare(arr, l, r)
        
        # Recursively apply quickSort to the left and right subarrays
        quickSort(arr, l, partition_index)
        quickSort(arr, partition_index + 1, r)
        
        return arr

def hoare(arr, l, r):
    # Choose the pivot element (first element in the subarray)
    pivot = arr[l]
    
    # Initialize indices for the Hoare partition scheme
    i = l - 1
    j = r + 1
    
    # Continue partitioning until the indices meet
    while True:
        # Move the left index to the right until arr[i] >= pivot
        i += 1
        while arr[i] < pivot:
            i += 1

        # Move the right index to the left until arr[j] <= pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If the indices meet or cross, return the partition index
        if i >= j:
            return j

        # Swap arr[i] and arr[j]
        arr[i], arr[j] = arr[j], arr[i]


# Example usage
arr = [8, 6, 7, 5, 4, 3, 9, 1, 2]
print("Original Array:", arr)
print("Sorted Array:", quickSort(arr, 0, len(arr) - 1))
