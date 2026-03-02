"""Given an integer array nums, return true if any value appears at 
least twice in the array, and return false if every element is distinct."""

def check_duplicates(nums):
    return len(nums) != len(set(nums))

nums = [1, 2, 3, 4, 5]
print(check_duplicates(nums)) # False

nums = [1, 2, 3, 2, 5]
print(check_duplicates(nums)) # True

def check_duplicates2(nums):
    dict = {}
    for num in nums:
        if num in dict:
            return True
        dict[num] = 1
    return False
nums = [1, 2, 3, 4, 5]
print(check_duplicates2(nums)) # False

nums = [1, 2, 3, 2, 5]
print(check_duplicates2(nums)) # Trues