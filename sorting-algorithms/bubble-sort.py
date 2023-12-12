def bubblesort(list_1):
    sorted = False  # Flag to track if any swaps were made in a pass
    
    # Continue iterating until no swaps are made in a pass
    while not sorted:
        sorted = True  # Assume the list is sorted until proven otherwise
        
        # Iterate through the list
        for i in range(0, len(list_1) - 1):
            # Compare adjacent elements and swap if they are in the wrong order
            if list_1[i] > list_1[i + 1]:
                sorted = False  # If a swap is made, set the flag to False
                list_1[i], list_1[i + 1] = list_1[i + 1], list_1[i]  # Swap elements
                
    return list_1

# Example usage
x = [9, 8, 12, 7, 6, 5, 4, 65, 10, 63, 87, 33, 2, 1]
print("Original List:", x)
print("Sorted List:", bubblesort(x))
