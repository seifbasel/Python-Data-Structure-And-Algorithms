def insertionsort(list):
    for i in range (0,len(list)):
        value_to_sort=list[i]
        while list[i-1] > value_to_sort and i>0:
            list[i], list[i-1] = list[i-1], list[i]
            i=i-1
    return list        





x = [1, 4, 6, 2, 8, 3, 4, 7, 10, 9, 34, 2, 3, 5, 8, 50, 0]
print(insertionsort(x))
