def quick_sort(lst):
    length = len(lst)
    
    # Base case: if the list has 1 or fewer elements, it is already sorted
    if length <= 1:
        return lst
    else:
        # Choose the pivot element as the last element in the list
        pivot = lst.pop()
        
        # Initialize two lists to hold elements greater and lower than the pivot
        items_greater = []
        items_lower = []

        # Iterate through the list and partition elements based on the pivot
        for item in lst:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)

        # Recursively apply quick_sort to the lower elements, concatenate with the pivot,
        # and then concatenate with the sorted greater elements
        return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

# Example usage
x = [9, 8, 12, 7, 6, 5, 4, 65, 10, 63, 87, 33, 2, 1]
print(quick_sort(x))
