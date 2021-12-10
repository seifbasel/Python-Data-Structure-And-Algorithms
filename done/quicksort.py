def quick_sort(list):
    length=len(list)
    if length <= 1:
        return list
    else:
        pivot=list.pop()
    item_greater=[]
    item_lower = []

    for item in list:
        if item > pivot:
            item_greater.append(item)
        else:
                item_lower.append(item)
    
    return quick_sort(item_lower)+ [pivot]+quick_sort(item_greater)


x = [9, 8, 12, 7, 6, 5, 4, 65, 10, 63, 87, 33, 2, 1]
print(quick_sort(x))

