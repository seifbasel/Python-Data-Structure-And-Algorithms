def binary_search(list,value):
    start=0
    end=len(list)
    mid=0
    for i in range (start,end):
        mid = (start+end)//2
        if value == list[mid]:
            return mid
        elif value < list[mid]:
            end=mid
        elif value > list[mid]:
            start=mid
    return i

print(binary_search([1,2,3,4,5,6,7,8,9],7))
