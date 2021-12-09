import math

def search(numbers, target):
    size = len(numbers)
    block_size = math.floor(math.sqrt(size))
    end = block_size
    start = 0
        
    while end < size and numbers[end] <= target:
        start = end
        end += block_size
        new_end = min(end, size)
    for i in range(start, new_end):
                if numbers[i] == target:
                    return True
            
                return False



