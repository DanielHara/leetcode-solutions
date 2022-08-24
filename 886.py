# Question 886: https://leetcode.com/problems/possible-bipartition/

"""
Something interesting about this question: I tried to solve it in February 2021, had a few failing submissions,
gave up on it and forgot about it. It can back to my mind today while I was reading the graph section "Algorithms" book
by Sedgwick, when he presents a simple algorithm to find out whether a graph is bipartite.

Basic build a graph where the dislikes are the edges, and then find out if there's any connected component which is not
bipartite. Actually quite simple once you see the equivalence of the problem with finding out whether a graph is bipartite.
"""

class Solution:
    # Explores the graph depth-first and returns False if the graph is not bipartite
    def explore(self, graph, visited, start, color):
        if start in visited:
            return True

        visited[start] = color
        for v in graph.get(start, []):
            if v in visited and visited[v] == visited[start]:
                return False

            if not self.explore(graph, visited, v, not color):
                return False
        
        return True
    
    
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = {}
        
        for [a, b] in dislikes: 
            if a not in graph:
                graph[a] = []
            
            graph[a].append(b)
            
            if b not in graph:
                graph[b] = []
            
            graph[b].append(a)
        
        visited = {}
        
        for i in range(1, n + 1, 1):
            if not self.explore(graph, visited, i, True):
                return False
        
        return True
