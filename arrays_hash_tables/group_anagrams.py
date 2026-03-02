"""Given an array of strings strs, group the anagrams together. 
You can return the answer in any order."""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for word in strs:
            word_sorted = "".join(sorted(word))
            if word_sorted in dict:
                dict[word_sorted].append(word)
            else:
                dict[word_sorted] = [word]
        return list(dict.values())



strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))

