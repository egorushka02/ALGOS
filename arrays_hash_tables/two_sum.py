"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

# Example 1:
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            print("i: ", i)
            print("nums[i]: ", nums[i])
            for j in range(i+1, len(nums)):
                print("j: ", j)
                print("nums[j]: ", nums[j])
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
            
#result = Solution().twoSum([2, 7, 11, 15], 9)
#result = Solution().twoSum([3, 2, 4], 6)
#print(result)

# Example 2:
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i in range(len(nums)):
            print(hash_table)
            complement = target - nums[i]
            if complement in hash_table:
                return [i, hash_table[complement]]
            hash_table[nums[i]] = i
        return None

result = Solution2().twoSum([2, 7, 11, 15], 9)
print(result)
result = Solution2().twoSum([3, 2, 4], 6)
print(result)