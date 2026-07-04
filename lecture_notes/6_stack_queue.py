"""
stack and queue
"""

"""
20. valid parentheses
example:
Input: s = "()"
Output: true   
Input: s = "()[]{}"
Output: true
Input: s = "(]"
Output: false
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []
        for c in s:
            if c in pair:
                stack.append(c)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if c != pair[prev]:
                    return False
        return len(stack) == 0
    

"""
1047. Remove All Adjacent Duplicates In String
example:
Input: s = "abbaca"
Output: "ca"
Input: s = "azxxzy"
Output: "ay"
"""
class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
    

"""
2390. Removing Stars From a String
example:
Input: s = "leet**cod*e"
Output: "lecoe"
Input: s = "erase*****"
Output: ""
"""
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if c == "*":
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
    
"""
71. Simplify Path
example:
Input: path = "/home/"
Output: "/home"
Input: path = "/../"
Output: "/"
Input: path = "/home//foo/"
Output: "/home/foo"
"""
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for p in path.split("/"):
            if p == "" or p == ".":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)
    
"""
933. Number of Recent Calls
example:
Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]
"""
from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.q = deque()
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)
        window = t - 3000
        while self.q and self.q[0] < window:
            self.q.popleft()
        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)