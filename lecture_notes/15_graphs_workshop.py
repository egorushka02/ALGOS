

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
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        if not mat:
            return mat

        n = len(mat)
        m = len(mat[0])

        seen = set()

        def is_not_valid(r, c):
            return r < 0 or c < 0 or r >= n or c >= m or (r, c) in seen

        queue = deque([])
            
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j, 1))
                    seen.add((i, j))

        while queue:
            r, c, d = queue.popleft()
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if not is_not_valid(r+dx, c+dy):
                    mat[r+dx][c+dy] = d
                    queue.append((r+dx, c+dy, d+1))
                    seen.add((r+dx, c+dy))
        
        return mat

"""
994. Rotting Oranges
"""
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        minutes = 0
        while queue and fresh:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row, next_col = row + dr, col + dc
                    if (0 <= next_row < rows and 0 <= next_col < cols and
                            grid[next_row][next_col] == 1):
                        grid[next_row][next_col] = 2
                        fresh -= 1
                        queue.append((next_row, next_col))
            minutes += 1

        return minutes if fresh == 0 else -1
