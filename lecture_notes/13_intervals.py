"""
Intervals
"""

"""
252. Meeting Rooms
"""
from typing import List

# O(nlogn) time complexity, O(1) space complexity
class Solution(object):
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        # 
        for i in range(1, len(intervals)):
            prev = intervals[i-1]
            current = intervals[i]
            if current[0] < prev[1]:
                return False
        return True

"""
56. Merge intervals
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            current = intervals[i]
            prev = merged[-1]
            if current[0] <= prev[1]:
                merged[-1][1] = max(prev[1], current[1])
            else:
                merged.append(current)
        return merged
    

# TODO: homework
"""
57. Insert interval
"""
# Stupid solution, need to fix it
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            current = intervals[i]
            prev = merged[-1]
            if current[0] <= prev[1]:
                merged[-1][1] = max(prev[1], current[1])
            else:
                merged.append(current)
        return merged
    

"""
253. Meetings   Rooms II
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        h = []
        intervals.sort()

        heappush(h, intervals[0][1])
        for i in range(1, len(intervals)):
            current = intervals[i]

            if current[o] >= h[0]:
                heappop(h)

            heappush(h, current[1])
        
        return len(h)