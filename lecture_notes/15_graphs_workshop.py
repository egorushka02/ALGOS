

"""
323. Number of connected components in an undirected graph
"""

from typing import List
from collections import defaultdict

"""
DFS
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()
        number = 0

        for i in range(n):
            if i not in seen:
                number += 1
                seen.add(i)

                stack = [i]
                while stack:
                    v = stack.pop()
                    for n in graph[v]:
                        if n not in seen:
                            seen.add(n)
                            stack.append(n)

        return number
    
"""
BFS
"""
from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()
        number = 0

        for i in range(n):
            if i not in seen:
                number += 1
                seen.add(i)

                queue = deque([i])
                while queue:
                    v = queue.popleft()
                    for n in graph[v]:
                        if n not in seen:
                            seen.add(n)
                            queue.append(n)

        return number


"""
547. Number of Provinces
"""
# TODO: not work, need to finish
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i]:
                    graph[i].append(j)
                    graph[j].append(i)

        seen = set()
        number = 0

        for i in range(n):
            if i not in seen:
                number += 1
                seen.add(i)

                queue = deque([i])
                while queue:
                    v = queue.popleft()
                    for n in graph[v]:
                        if n not in seen:
                            seen.add(n)
                            queue.append(n)

        return number
    
"""
200. Number of Islands
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        
        number = 0
        n = len(grid)
        m = len(grid[0])

        def is_not_valid(r, c):
            return r < 0 or c < 0 or r >= n or c >= m or grid[r][c] != '1'
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    number += 1

                    queue = deque([(i, j)])
                    while queue:
                        r, c = queue.popleft()
                        # check
                        if not is_not_valid(r, c):
                            grid[r][c] = '0'
                            queue.append((r+1, c))
                            queue.append((r-1, c))
                            queue.append((r, c+1))
                            queue.append((r, c-1))

        return number
    

"""
1466. Reorder Routes to Make All Paths Lead to the City Zero
"""
class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        og_directions = set()
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            og_directions.add((a, b))

        turns = 0

        seen = {0}
        stack = [0]
        while stack:
            v = stack.pop()
            for n in graph[v]:
                if n not in seen:
                    if (v, n) in og_directions:
                        turns += 1
                    stack.append(n)
                    seen.add(n)


        return turns

# TODO: homework
"""
695. Max Area of Island
"""


"""
2368. Reacheble Nodes With Restrictions
"""
class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set(restricted)
        seen.add(0)

        result = 0

        stack = [0]
        while stack:
            v = stack.pop()
            result += 1
            for n in graph[v]:
                if n not in seen:
                    seen.add(n)
                    stack.append(n)

        return result
    
"""
542. 01 Matrix
"""
