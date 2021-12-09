import math

def jumpsearch(list, target):
    start = 0
    end = len(list)
    jump = int(math.sqrt(len(list)))
    for i in range(start, end, jump):
        if list[i] == target:
            return i
        elif target > list[i]:
            start =+jump
            end = len(list)
        elif target < list[i]:
            end = jump
        
        return i

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15]

res = jumpsearch(list1, 3)
print(res)
