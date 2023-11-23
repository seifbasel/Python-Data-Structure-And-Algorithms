def binarysearch(list, search_value):
    start = 0
    last = len(list)
    for i in range(start, last):
        mid = (start+last)//2
        if search_value == list[mid]:
            return mid
        elif search_value < list[mid]:
            last = mid
        elif search_value > list[mid]:
            start = mid
    return i


x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binarysearch(x, 8))
