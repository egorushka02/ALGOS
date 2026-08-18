"""
Backtracking
"""

"""
46. Permutations
"""
# TODO: rewrite with set
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(acc):
            if len(acc) == len(nums):
                result.append(acc[:])
            for num in nums:
                if num not in acc:
                    acc.append(num)
                    backtrack(acc)
                    acc.pop()

        backtrack([])
        return result
    

"""
77. Combinations
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(acc, start):
            if len(acc) == k:
                result.append(acc[:])
                return
            for num in range(start, n+1):
                acc.append(num)
                backtrack(acc, num+1)
                acc.pop()
        
        backtrack([], 1)
        return result
    

"""
78. Subsets
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        n = len(nums)
        def backtrack(acc, start):
            if start > n:
                return
            
            result.append(acc[:])

            for i in range(start, n):
                acc.append(nums[i])
                backtrack(acc, i+1)
                acc.pop()
        
        backtrack([], 0)
        return result
    

"""
22. Generate Parentheses
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def backtrack(acc, op, cl): # op-open, cl-close
            if len(acc) == 2*n:
                result.append(acc)
                return
        
            #  !!!!!!!!!!!THINK ABOUT IT!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if op < n:   
                backtrack(acc + "(", op+1, cl)
            if cl < op:
                backtrack(acc + ")", op, cl+1)

        backtrack("", 0, 0)
        return result