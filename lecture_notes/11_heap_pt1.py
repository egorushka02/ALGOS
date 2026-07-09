"""
Priority Queue and Heap
"""

import heapq

min_heap = [2, 41, 5, 2, 5, 6 , 8]
heapq.heapify(min_heap)

print(min_heap)

heapq.heappush(min_heap, 0)
print(min_heap)
print(heapq.heappop(min_heap))
print(min_heap)

arr = [4, 1, 5, 8, 10, 0, 12]
max_heap = []
for num in arr:
    heapq.heappush(max_heap, -num)
print(max_heap)

print(-heapq.heappop(max_heap))

"""
215. Kth Largest Element in an Array
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
    
"""
703. Kth Largest Element in a Stream
"""
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.min_heap = nums
        self.k = k

        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

"""
347. Top K Frequent Elements
"""
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = Counter(nums)
        min_heap = []
        for num, freq in c.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [item[1] for item in min_heap]
    
"""
451. Sort Characters By Frequency
"""
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = Counter(s)
        max_heap = []
        for ch, value in c.items():
            heapq.heappush(max_heap, (-value, ch*value))
        result = ""
        while max_heap:
            result += heapq.heappop(max_heap)[1]
        return result