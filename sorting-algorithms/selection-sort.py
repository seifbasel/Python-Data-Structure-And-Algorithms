def selectionsort(lst):
    # Iterate through the entire list
    for i in range(0, len(lst)):
        # Assume the current index has the minimum value
        min_value_index = i

        # Check for a smaller element in the rest of the list
        for j in range(i + 1, len(lst)):
            # Update the minimum value index if a smaller element is found
            if lst[j] < lst[min_value_index]:
                min_value_index = j

        # Swap the found minimum element with the element at the current index
        if min_value_index != i or min_value_index < i:
            lst[min_value_index], lst[i] = lst[i], lst[min_value_index]

    return lst

# Example usage
list_1 = [9, 8, 6, 5, 3, 2, 1, 18, 55, 33, 62, 75, 15, 47, 38, 498]
print("Original List:", list_1)
print("Sorted List:", selectionsort(list_1))
