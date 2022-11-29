def insertionsort(list_1):
    # loop throught elements of list
    for i in range (0,len(list_1)):
        value_to_be_sort=list_1[i]
        
        while value_to_be_sort < list_1[i-1] and i>0:
            list_1[i], list_1[i-1] = list_1[i-1], list_1[i]
            i=i-1

    return list_1
            
x = [1,9,2,8,3,7,4,6,5,10]
print(insertionsort(x))