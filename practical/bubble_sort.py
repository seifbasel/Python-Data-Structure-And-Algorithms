def bubble_sort(list):
    start=0
    end=len(list)-1
    sorted=False
    while not sorted:
        sorted = True
        for i in range(start,end):
            if list[i+1]<list[i]:
                sorted=False
                list[i+1],list[i]=list[i],list[i+1]
    return list



print(bubble_sort([9,5,7,1,8,2,3,4,0,10,6]))