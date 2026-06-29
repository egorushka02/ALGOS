

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        print(mid)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid-1
        else:
            low = mid+1
    return None
    
my_list = [1, 2, 5, 7, 9, 11, 12, 15, 23]

print(binary_search(my_list, 9))
#print(binary_search(my_list, 10))