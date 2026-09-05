"""
Dynamic Programming Part 2
"""

"""
91. Decode Ways
"""
# TODO: rewrite using cache
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def inner(s):
            if len(s) == 0:
                return 1
            if s[0] == "0":
                return 0
            if len(s) == 1:
                return 1
            if s[:2] > "26":
                return inner(s[1:])
            return inner(s[1:]) + inner(s[2:])

        return inner(s)


"""
62. Unique Paths
"""
# 2d dynamic programming
# TODO: optimize
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # should replace n and m, now it is transposed
        dp = [[1]*m for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
        return dp[n-1][m-1]


"""
64. Minimum Path Sum
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        dp = [[0] * m for _ in range(n)]

        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + grid[i-1][0]
        for j in range(1, m):
            dp[0][j] = dp[0][j-1] + grid[0][j-1]
        
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i-1][j] + grid[i-1][j], dp[i][j-1] + grid[i][j-1])
        
        return dp[n-1][m-1] + grid[n-1][m-1]