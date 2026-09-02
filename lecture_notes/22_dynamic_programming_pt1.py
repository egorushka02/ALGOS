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