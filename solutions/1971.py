# Question 1971: https://leetcode.com/problems/find-if-path-exists-in-graph/

"""
    Quite trivial question, just explore the graph starting at source, and check if destination is visited after the exploration.
"""

class Solution:
    def explore(self, graph, source, visited):
        if source in visited:
            return
        
        visited.add(source)
        
        for vertex in graph.get(source, []):
            self.explore(graph, vertex, visited)
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        
        for [a, b] in edges:
            if a not in graph:
                graph[a] = []
            
            graph[a].append(b)
            
            if b not in graph:
                graph[b] = []
            graph[b].append(a)
        
        visited = set()
        
        self.explore(graph, source, visited)
        
        return destination in visited
