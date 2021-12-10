import math

def search(list, target):
    size = len(list)
    jump_value = math.floor(math.sqrt(size))
    end = jump_value
    start = 0
        
    while end < size and list[end] <= target:
        start = end
        end += jump_value
        new_end = min(end, size)
    for i in range(start, new_end):
                if list[i] == target:
                    return True
            
                return False

