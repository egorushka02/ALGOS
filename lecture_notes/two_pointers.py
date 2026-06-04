

"""
Reverse a string using the two pointers technique.
"""
class Solution:
    def revesreString(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return
    
"""
is palindrome
"""

class Solution:
    def isPalindrome(self, s):
        # isalnum() checks if the character is alphanumeric
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

"""
Two sum II - input array is sorted
"""
class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left+1, right+1]
            if current_sum > target:
                right -= 1
            else:
                left += 1
        return  []
    
"""
3sum
"""
class Solution:
    def threeSum(self, nums):
        nums = sorted(nums) # O(nlogn)
        result = ()
        n = len(nums)
        for i in range(n):
            target = -nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    result.add((target, nums[left], nums[right]))
                if current_sum > target:
                    right -= 1
                else:
                    left += 1
        return result

"""
Squares of a sorted array
"""
class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1

        for i in range(n-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                result[i] = nums[right] * nums[right]
                right -= 1
            else:
                result[i] = nums[left] * nums[left]
                left += 1

        return result
    

"""
check this out
max area of a container
"""
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area