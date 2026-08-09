"""
part 2
"""

"""
1129. Shortest Path with Alternating Colors
"""
from collections import defaultdict
from collections import deque

class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        RED = 0
        BLUE = 1

        graph = defaultdict(lambda: defaultdict(list))
        for a, b in redEdges:
            graph[RED][a].append(b)
        for a, b in blueEdges:
            graph[BLUE][a].append(b)

        result = [float('inf')] * n
        result[0] = 0

        queue = deque([(0, RED, 0), (0, BLUE, 0)])
        seen = {(0, RED), (0, BLUE)}

        while queue:
            v, color, depth = queue.popleft()
            result[v] = min(result[v], depth)

            for n in graph[color][v]:
                if (n, 1-color) not in seen:
                    seen.add((n, 1-color))
                    queue.append((n, 1-color, depth+1))

        return [x if x != float('inf') else -1  for x in result]
    

"""
1926. Nearest Exit from Entrance in Maze
"""
from typing import List
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])

        e_r, e_c = entrance # entrance_row, entrance_col
        maze[e_r][e_c] = "+"
        queue = deque([(e_r, e_c, 0)])

        while queue:
            r, c, num = queue.popleft()
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_r = r + dr
                new_c = c + dc

                if 0 <= new_r < rows and 0 <= new_c < cols and maze[new_r][new_c] == ".":
                    if new_r == 0 or new_r == rows-1 or new_c == 0 or new_c == cols-1:
                        return num + 1
                    maze[new_r][new_c] = "+"
                    queue.append((new_r, new_c, num + 1))
        return -1
    

"""
1091. Shortest Path in Binary Matrix
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1:
            return -1

        grid[0][0] = 1
        queue = deque([(0, 0, 1)])

        while queue:
            r, c, num = queue.popleft()
            if r == rows-1 and c == cols-1:
                return num

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                new_r = r + dr
                new_c = c + dc

                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 0:
                    if new_r == rows-1 and new_c == cols-1:
                        return num + 1
                    grid[new_r][new_c] = 1
                    queue.append((new_r, new_c, num + 1))
        return -1

"""
752. Open the Lock
"""
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if "0000" in deadends:
            return -1

        queue = deque([("0000", 0)])
        seen = set(deadends)

        def neighbours(current):
            result = []
            for i in range(4):
                num = int(current[i])
                for d in [-1, 1]:
                    x = (num + d) % 10
                    result.append(current[:i] + str(x) + current[i+1:])

            return result

        while queue:
            current, steps = queue.popleft()
            if current == target:
                return steps
            for n in neighbours(current):
                if n not in seen:
                    queue.append((n, steps+1))
                    seen.add(n)

        return -1

# TODO: homework 
"""
433. Minimum Genetic Mutation
"""


"""
994. Rotting Oranges
"""
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        fresh_counts = 0
        minutes = 0

        queue = deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_counts += 1
                if grid[i][j] == 2:
                    queue.append((i, j, minutes))
        while queue:
            i, j, minutes = queue.popleft()
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_i = i + di
                new_j = j + dj
                
                if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] == 1:
                    fresh_counts -= 1
                    grid[new_i][new_j] = 2
                    queue.append((new_i, new_j, minutes+1))

        if fresh_counts == 0:
            return minutes
        return -1
        