"""
Block A
"""

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
    
"""
Block B
"""

"""
Removde duplicates from sorted array
"""
class Solution:
    def removeDuplicates(self, nums):
        k = 0
        for i in range(len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
        return k + 1
    
# nums = [0,0,1,1,1,2,2,3,3,4]
# solution = Solution()
# print(solution.removeDuplicates(nums))
# print(nums)

"""
Move zeroes
"""
class Solution:
    def moveZeroes(self, nums):
        """
        *
        [0, 1, 2, 3, 0, 12]
            *
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1


# nums = [0,1,0,3,12]
# solution = Solution()
# print(solution.moveZeroes(nums=nums))   
# print(nums)

"""
Block C
"""

"""
is subsequence
"""
class Solution:
    def isSubsequence(self, s, t):
        p1 = 0
        p2 = 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1

        return p1 == len(s)
    
"""
merge sorted array
"""
class Solution:
    def merge(self, nums1, m, nums2, n):
        result = []
        p1 = 0
        p2 = 0

        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
            else:
                result.append(nums2[p2])
                p2 += 1
        for k in range(p1, m):
            result.append(nums1[k])

        for k in range(p2, n):
            result.append(nums2[k])