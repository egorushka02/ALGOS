"""
Given an integer array nums, return an array answer such that answer[i] is 
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        print(nums)
        n = len(nums)
        left, right, answer = [1]*n, [1]*n, [1]*n
        
        for i in range(1, n):
            left[i] = nums[i-1] * left[i-1]
        
        for j in range(n-2, -1, -1):
            right[j] = nums[j+1] * right[j+1]
        
        for k in range(n):
            answer[k] = left[k] * right[k]
        print(left)
        print(right)
        
        return answer
print(Solution().productExceptSelf([1,2,3,4]))


        
