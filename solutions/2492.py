"""
    Question 2492: https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

    Interesting question! Actually, find all nodes in the connected graph containing node 1.
    Then, you can create a path containing all possible edges, in order to create the path with the minimum score.
"""

class Solution:
    def recursiveExplore(self, graph, origin, visited):
        if origin in visited:
            return
        
        visited.add(origin)
        
        for [neighbour, distance] in graph.get(origin, []):
            self.recursiveExplore(graph, neighbour, visited)

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        result = None
        graph = {}

        for [origin, destination, distance] in roads:
            if origin not in graph:
                graph[origin] = []
            graph[origin].append([destination, distance])

            if destination not in graph:
                graph[destination] = []
            graph[destination].append([origin, distance])

        visited = set()
        self.recursiveExplore(graph, 1, visited)

        result = None
        for node in visited:
            for [neighbours, distance] in graph.get(node, []):
                result = min(result, distance) if result is not None else distance
        
        return result
