def selectionsort(list):
    
    for i in range(0,len(list)):
        min_value = i
        
        for j in range(i+1,len(list)):
            
            if list[j] < list[min_value]:
                min_value = j
        if min_value != i or min_value < i:
            list[min_value],list[i] =list[i],list[min_value]
            
    return list        
list_1=[9,8,6,5,3,2,1,18,55,33,62,75,15,47,38,498]
print(selectionsort(list_1))