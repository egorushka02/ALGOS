"""
Dynamic Programming part 1
"""

"""
509. Fibonacci Number
"""
# V1
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)

# V2
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        def inner(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n in cache:
                return cache[n]
            cache[n] = inner(n-1) + inner(n-2)
            return cache[n]
        return inner(n)

# V3
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

# V4
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        a = 0
        b = 1
        for i in range(2, n+1):
            tmp = a + b
            a = b
            b = tmp
        return b


"""
70. Climbing Stairs
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        def inner(n):
            if n == 0:
                return 1
            if n == 1:
                return 1
            if n in cache:
                return cache[n]
            cache[n] = inner(n-1) + inner(n-2)
            return cache[n]
        return inner(n)


 """
 746. Min Cost Climbing Stairs
 """
# from up to bottom
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cache = {}
        n = len(cost)

        def inner(n):
            if n <= 1:
                return 0
            if n in cache:
                return cache[n]
            cache[n] = min(inner(n-1) + cost[n-1], inner(n-2) + cost[n-2])
            return cache[n]

        return inner(n)

# from bottom to up
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [0] * (n+1)
        
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            

        return dp[n]

"""
322. Coin Change
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)

        if dp[amount] == float('inf'):
            return -1
        return dp[amount]

"""
198. House Robber
"""
# v1
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        def inner(nums):
            n = len(nums)
            if n == 0:
                return 0
            if n == 1:
                return nums[0]
            if n in cache:
                return cache[n]
            cache[n] = max(nums[0] + inner(nums[2:]), inner(nums[1:]))
            return cache[n]

        return inner(nums)

# v2
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]

        for i in range(2, n + 1):
            dp[i] = max(nums[i-1] + dp[i-2], dp[i-1])

        return dp[n]

# v3
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        b = 0

        for num in nums:
            tmp = max(a + num, b)
            a = b
            b = tmp
            

        return b