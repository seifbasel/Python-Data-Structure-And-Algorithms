def linearsearch(array,search_item,):
    for i in range(0,len(array)):
       if array[i]==search_item:

          return i

    return -1


array =[1,3,6,9,10,13,17,20]

result =linearsearch(array,17)
print("the element index is ",result)
