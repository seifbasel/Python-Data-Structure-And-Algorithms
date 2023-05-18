import math

def jump_search_2(arr, search):

    jump = int(math.sqrt(len(arr)))

    ''' find last lowest element '''
    for i in range(0, len(arr), jump):
        if arr[i] < search:
            low = i
        elif arr[i] == search:
            return i
        else:
            break
    ''' apply linear search '''
    l_index = [e for e, i in enumerate(arr[low:low+jump]) if i == search]
    if l_index[0]:
        return low+l_index[0]
    return "Not Found"

arr = [i for i in range(1, 300)]
res = jump_search_2(arr, 16)
print(res)
