

"""
2101. Detonate the Maximum Bombs
"""


"""
752.
"""


"""
433.    
"""

"""
841. Keys and Rooms
"""
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        def traverse(room):
            for neighbour in rooms[room]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    traverse(neighbour)
        seen = {0}
        traverse(0)
        return len(seen) == len(rooms)
    
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        seen = {0}
        stack = [0]

        while stack:
            room = stack.pop()
            for neighbour in rooms[room]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    stack.append(neighbour)
        
        return len(seen) == len(rooms)
    

"""
1971. Find if Path Exists in Graph
"""
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # 0: [1, 2]
        # 1: [0, 2]
        # 2: [0, 1]
        seen = set()
        seen.add(source)
        stack = [source]
        while stack:
            v = stack.pop()
            if v == destination:
                return True
            for n in graph[v]:
                if n not in seen:
                    seen.add(n)
                    stack.append(n)
        return False
    
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # 0: [1, 2]
        # 1: [0, 2]
        # 2: [0, 1]
        seen = set()
        seen.add(source)
        queue = deque([source])
        while queue:
            v = queue.popleft()
            if v == destination:
                return True
            for n in graph[v]:
                if n not in seen:
                    seen.add(n)
                    queue.append(n)
        return False
    
"""
133. Clone Ggraph
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        
        seen = {}
        stack = [node]
        seen[node] = Node(node.val, [])
        while stack:
            v = stack.pop()
            for n in v.neighbors:
                if n not in seen:
                    seen[n] = Node(n.val, [])
                    stack.append(n)
                seen[v].neighbors.append(seen[n])


        return seen[node]
    

"""
1557. Minimum Number of Vertices to Reach All Nodes
"""
class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        in_degree = [0] * n
        for _, to in edges:
            in_degree[to] += 1
        return [node for node in range(n) if in_degree[node]==0]