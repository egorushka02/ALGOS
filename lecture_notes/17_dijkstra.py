"""
Dijkstra's algorithm
"""


"""
743. Network Delay Time
"""
from collections import defaultdict
from heapq import heappop, heappush


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        for a, b, w in times:
            graph[a].append((b, w))

        min_heap = [(0, k)]
        distances = {}
        distances[k] = 0

        while min_heap:
            dst, node = heappop(min_heap)
            if dst > distances.get(node, float('inf')):
                continue

            for ngh, dst_to_ngh in graph[node]:
                new_dst = dst + dst_to_ngh
                if new_dst < distances.get(ngh, float('inf')):
                    distances[ngh] = new_dst
                    heappush(min_heap, (new_dst, ngh))
        if n != len(distances):
            return -1

        return distances[max(distances, key=lambda x: distances[x])]
    

"""
1514. Path with Maximum Probability
"""
class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        graph = defaultdict(list)
        for i in range(len(edges)):
            a = edges[i][0]
            b = edges[i][1]
            p = succProb[i]
            graph[a].append((b, p))
            graph[b].append((a, p))

        max_heap = [(-1.0, start_node)]
        probs = {}
        probs[start_node] = 1.0

        while max_heap:
            p, node = heappop(max_heap)
            if node == end_node:
                return -p

            for ngh, p_to_ngh in graph[node]:
                new_prob = p_to_ngh * -p
                if ngh not in probs or new_prob > probs[ngh]:
                    probs[ngh] = new_prob
                    heappush(max_heap, (-new_prob, ngh))

        return 0

        
"""
787. Cheapest Flights Within K Stops
"""
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        g = defaultdict(list)
        for a, b, c in flights:
            g[a].append((b, c))

        stops = {}
        min_heap = [(0, 0, src)] 
        while min_heap:
            cost, depth, flight = heappop(min_heap)
            if depth > k + 1:
                continue

            if flight == dst:
                return cost

            stops[flight] = depth
            for ngh, cost_to_ngh in g[flight]:
                if ngh not in stops or depth + 1 <= stops[ngh]:
                    heappush(min_heap, (cost + cost_to_ngh, depth+1, ngh))

        return -1