"""
Given an integer array nums and an integer k, return the k most
frequent elements. You may return the answer in any order.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        result = sorted(dict, key = lambda x: dict[x], reverse=True)
        return result[:k]
    
print(Solution().topKFrequent([1,1,1,2,2,3], 2))