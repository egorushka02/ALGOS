"""Given two strings s and t, return true if t is an anagram of s, and false otherwise."""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(s)
        t = sorted(t)
        return s == t
    
result = Solution().isAnagram("anagram", "nagaram")
print(result)

class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1, dict2 = {}, {}
        for char in s:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1
        for char in t:
            if char in dict2:
                dict2[char] += 1
            else:
                dict2[char] = 1
        return dict1 == dict2
result = Solution2().isAnagram("anagram", "nagaram")
print(result)
