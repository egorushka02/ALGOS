

# def sum_arr(arr):
#     total = 0
#     for x in arr:
#         total += x
#     return total

# print(sum_arr([2, 3, 5]))

# TODO: доделать
# def recursion_sum(arr):
#     total = 0
#     print(arr)
#     if len(arr) == 1:
#         total += arr[0]
#     else:
#         total += recursion_sum(arr)
#     return total

# print(recursion_sum([2, 5, 6]))


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0] # рекурсивный случай
        less = [i for i in array[1:] if i < pivot]

        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([2, 0, 9, -2, 65, 8]))