def insertionsort(list_1):
    # Loop through elements of the list
    for i in range(1, len(list_1)):

        # Keep swapping the current element with the previous until in the correct order
        while list_1[i - 1] > list_1[i] and i > 0:
            list_1[i], list_1[i - 1] = list_1[i - 1], list_1[i]
            i = i - 1

    return list_1

# Example usage
x = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10]
print("Original List:", x)
print("Sorted List:", insertionsort(x))
