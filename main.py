import heapq
from typing import Dict, List, Tuple


def dijkstra(graph: Dict[str, List[Tuple[str, int]]], start: str) -> Dict[str, int]:
    """
    Find shortest paths from start node to all other nodes using Dijkstra's algorithm.
    
    Args:
        graph: Adjacency list where graph[node] = [(neighbor, weight), ...]
        start: Starting node
    
    Returns:
        Dictionary mapping each node to its shortest distance from start
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_dist > distances[current_node]:
            continue
        
        for neighbor, weight in graph.get(current_node, []):
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances


def dijkstra_with_path(graph: Dict[str, List[Tuple[str, int]]], start: str, end: str) -> Tuple[int, List[str]]:
    """
    Find shortest path from start to end using Dijkstra's algorithm.
    
    Returns:
        Tuple of (distance, path as list of nodes)
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_node == end:
            break
        
        if current_dist > distances[current_node]:
            continue
        
        for neighbor, weight in graph.get(current_node, []):
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    if distances[end] == float('inf'):
        return -1, []
    
    return distances[end], path


if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    
    distances = dijkstra(graph, 'A')
    print("Shortest distances from A:", distances)
    
    dist, path = dijkstra_with_path(graph, 'A', 'D')
    print(f"Shortest path A -> D: {path} (distance: {dist})")
