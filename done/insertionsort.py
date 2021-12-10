def insertionsort(list_1):
    
    for i in range (0,len(list_1)):
        value_to_sort=list_1[i]
        
        while list_1[i-1] > value_to_sort and i>0:
            list_1[i], list_1[i-1] = list_1[i-1], list_1[i]
            i=i-1 
    
    return list_1        
            

x = [1, 4, 6, 2, 8, 3, 4 , 7 , 10 , 9, 34, 2, 3, 5, 8,50,0 ]
print(insertionsort(x))
