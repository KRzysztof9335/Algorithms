"""https://www.algoexpert.io/questions/dijkstra's-algorithm
Type: Famous algorithms
"""
from typing import List, Set, Tuple

def dijkstrasAlgorithm(start: int, edges: List[List[List[int]]]) -> List[int]:
    """Edges is a list of nodes, where node number is index in list. Specific node
    has list of pair [destination, weight] to nodes it can go"""
    # Setup distances. The distance of start node to itself is always 0
    distances: List[int] = [-1 for _ in range(0, len(edges))]
    distances[start] = 0

    edges_traversed: Set[Tuple[int, int, int]] = set()
    edges_to_traverse: List[Tuple[int, int, int]] = []

    append_to_traverse(edges, start, edges_to_traverse, edges_traversed)
    while edges_to_traverse:
        to_traverse = edges_to_traverse.pop(0)
        edges_traversed.add(to_traverse)

        start_node = to_traverse[0]
        next_node = to_traverse[1]
        weight = to_traverse[2]

        dist = distances[start_node] + weight

        if distances[next_node] == -1 or dist < distances[next_node]:
            distances[next_node] = dist

        append_to_traverse(edges, next_node, edges_to_traverse, edges_traversed)

    return distances

def append_to_traverse(edges: List[List[List[int]]],
                       node: int,
                       to_traverse: List[Tuple[int, int, int]],
                       edges_traversed: Set[Tuple[int, int, int]]):
    "Method does modify input in place"
    for edge in edges[node]:
        edge_to_traverse = (node, edge[0], edge[1])
        if edge_to_traverse in edges_traversed:
            continue
        to_traverse.append(edge_to_traverse)