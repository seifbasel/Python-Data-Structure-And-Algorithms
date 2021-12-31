def bubble_sort(list):
    start = 0
    end = len(list)
    for i in range(start,end):
        for j in range(i+1, end):
            if list[j] < list[i]:
                list[j], list[i] = list[i], list[j]
    return list


print(bubble_sort([9, 5, 7, 1, 8, 2, 3, 4, 0, 10, 6]))
