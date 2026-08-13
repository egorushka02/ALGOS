"""
Topological Sort part 2
"""

"""
207. Course Schedule
"""
from collections import defaultdict, deque
from typing import List


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        g = defaultdict(list)
        in_degree = defaultdict(int)

        for a, b in prerequisites:
            g[b].append(a)
            in_degree[a] += 1

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        n = 0
        while queue:
            node = queue.popleft()
            n += 1
            for ngh in g[node]:
                in_degree[ngh] -= 1
                if in_degree[ngh] == 0:
                    queue.append(ngh)

        return n == numCourses
    

"""
210. Course Schedule II
"""
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        g = defaultdict(list)
        in_degree = defaultdict(int)

        for a, b in prerequisites:
            g[b].append(a)
            in_degree[a] += 1

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for ngh in g[node]:
                in_degree[ngh] -= 1
                if in_degree[ngh] == 0:
                    queue.append(ngh)

        if len(order) == numCourses:
            return order
        else:
            return []
        

"""
1136. Parallel Courses
"""
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        g = defaultdict(list)
        in_degree = defaultdict(int)

        for a, b in relations:
            g[a].append(b)
            in_degree[b] += 1

        queue = deque()
        for i in range(1, n+1):
            if in_degree[i] == 0:
                queue.append(i)

        semesters = 0
        while queue:
            level = len(queue)
            for _ in range(level):
                node = queue.popleft()
                n -= 1
                for ngh in g[node]:
                    in_degree[ngh] -= 1
                    if in_degree[ngh] == 0:
                        queue.append(ngh)
            semesters += 1
        
        if n == 0:
            return semesters
        else:
            return -1
