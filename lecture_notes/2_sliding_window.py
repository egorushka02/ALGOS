"""
sliding window pattern

  x x x x x x x
  [    ]


"""


"""
643. Maximum Average Subarray I
"""
# from typing import List
# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         begin = 0
#         window_state = 
#         for end in range(len(nums)):
#             [0, 1, 2, 3, 4]
#             end = 4
#             begin = 1

#             end-begin+1 # window size


#             if # window condition
#               begin += 1 # shrink window

from collections import defaultdict
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        begin = 0
        window_state = 0
        result = float('-inf')

        for end in range(len(nums)):
            window_state += nums[end]

            if end - begin + 1 == k:
                result = max(result, window_state)
                window_state -= nums[begin]
                begin += 1 # shrink window        
        return result/k

# solution = Solution()
# nums = [1, 12, -5, -6, 50, 3]
# print(solution.findMaxAverage(nums=nums, k=4))
# nums = [5]
# print(solution.findMaxAverage(nums=nums, k=1))

"""
209. Minimum size subarray size
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        begin = 0
        window_state = 0
        result = float('inf')

        for end in range(len(nums)):
            window_state += nums[end]

            while window_state >= target:
                window_size = end - begin + 1
                result = min(result, window_size)
                window_state -= nums[begin]
                begin += 1

        if result == float('inf'):
            return 0
        return result
# solution=Solution()
# nums = [2, 3, 1, 2, 4, 3]
# target = 7
# print(solution.minSubArrayLen(target=target, nums=nums))
# nums = [1, 4, 4]
# target = 4
# print(solution.minSubArrayLen(target=target, nums=nums))
# nums = [1, 1, 1, 1, 1, 1, 1]
# target = 11
# print(solution.minSubArrayLen(target=target, nums=nums))


"""
1004. Max Consequtive ones
"""
class Solution:
    def longestConsequtive(self, nums: List[int], k: int) -> int:
        begin = 0
        window_state = 0 # how much 0 ?
        result = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                window_state += 1
            
            while window_state > k:   # window condition 0? >k
                if nums[begin] == 0:
                    window_state -= 1
                begin += 1

            result = max(result, end-begin+1)

        return result
# solution=Solution()
# nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
# k = 2
# print(solution.longestConsequtive(nums=nums, k=k))



"""
1493. Longest Subarray of 1's After Deleting One Element
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        begin = 0
        window_state = 0 # how much 0 ?
        result = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                window_state += 1

            while window_state > 1: # window condition
                if nums[begin] == 0:
                    window_state -= 1
                begin += 1
            
            result = max(result, end-begin+1)

        return result - 1 # we have to delete one element
# solution = Solution()
# nums = [1, 1, 0, 1]
# print(solution.longestSubarray(nums=nums))

"""
904. Fruit into Baskets
"""

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        begin = 0
        window_state = defaultdict(int)
        result = 0

        for end in range(len(fruits)):
            window_state[fruits[end]] += 1
            while len(window_state) > 2:
                window_state[fruits[begin]] -= 1
                if window_state[fruits[begin]] == 0:
                    del window_state[fruits[begin]]
                begin += 1 # shrink
        return result

# fruits = [1, 2, 3, 2, 2]
# solution = Solution()
# print(solution.totalFruit(fruits=fruits))
                
