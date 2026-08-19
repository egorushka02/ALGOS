"""
Backtracking part 2
"""

"""
216. Combination Sum III
"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []

        def bt(start, acc, path_sum):
            if len(acc) == k:
                if path_sum == n:
                    result.append(acc[:])
                return

            if path_sum > n:
                return
            
            for num in range(start, 10):
                acc.append(num)
                bt(num+1, acc, path_sum+num)
                acc.pop()

        bt(1, [], 0)

        return result