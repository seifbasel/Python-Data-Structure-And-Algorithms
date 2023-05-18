def bubblesort(list_1):
    sorted =False
    while not sorted:
        sorted=True
        for i in range(0,len(list_1)-1):
            if list_1[i]>list_1[i+1]:
                sorted=False
                list_1[i], list_1[i+1] = list_1[i+1],list_1[i]
    return list_1            
        
x=[9,8,12,7,6,5,4,65,10,63,87,33,2,1]
print(bubblesort(x))