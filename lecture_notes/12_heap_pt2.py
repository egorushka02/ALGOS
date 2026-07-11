"""
heap pt 2
"""

"""
1046. Last Stone Weight
"""

import heapq
from math import floor

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if first != second:
                heapq.heappush(stones, -(first-second))
        
        if not stones:
            return 0
        return -stones[0]
    

"""
502. IPO
"""
import heapq
# TODO: look again
class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        """
        Мы смотрим на проекты на который хватает денег
        и из них выбираем максимальный профит
        """
        projects = [(cost, profit) for profit, cost in zip(profits, capital)]
        projects.sort()
        sorted_projects = []
        i = 0
        # don't iterate more than 3 times
        while projects and k > 0:
            while i < len(projects) and w - projects[i][0] >= 0:
                heappush(sorted_projects, -projects[i][1])
                i += 1
            if not sorted_projects:
                break
            
            w += -heappop(sorted_projects)
            k -= 1

        return w
    

"""
295. Find Median from Data Stream
"""
# Doesn't work for some reason, but the logic is correct
class MedianFinder(object):

    def __init__(self):
        self.max_heap = [] # [*****,,,,,]
        self.min_heap = [] # [,,,,,*****]


    def addNum(self, num): # O(logn)
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        # сначала порядок: max_heap[0] должен быть <= min_heap[0]
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))


    def findMedian(self): # O(1)
        """
        :rtype: float
        """
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (self.min_heap[0] + -self.max_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

"""
1962. Remove Stones to Minimize the Total
"""
# TODO: finish
class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        heap = [- pile for pile in piles]
        heapq.heapify(heap)

        for _ in range(k):
            -floor(heapq.heappop(heap)/2)


"""
23. Merge k Sorted Lists
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy
        min_heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))
        while min_heap:
            val, i = heapq.heappop(min_heap)
            current.next = lists[i]
            current = current.next

            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(min_heap, (lists[i].val, i))
        return dummy.next