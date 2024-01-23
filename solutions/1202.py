"""
Question 1202: https://leetcode.com/problems/smallest-string-with-swaps/

Make a graph and get the connected components, and greedily out the lexicographically lowest chars
in the first positions.
"""

class Solution:
    def exploreConnectedComponent(self, start: int, marked, graph, i: int):
        if start in marked:
            return None
        
        marked[start] = i
        
        for v in graph.get(start, []):
            self.exploreConnectedComponent(v, marked, graph, i)
    
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # Transform string into array:
        array = [*s]

        # Transform pairs into graph:
        graph = {}
        for [a, b] in pairs:
            if a not in graph:
                graph[a] = [b]
            else:
                graph[a].append(b)
            
            if b not in graph:
                graph[b] = [a]
            else:
                graph[b].append(a)
        
        
        # A "Connected Component" is actually a set
        connected_components = []
        
        marked = {}
        for i in range(len(s)):
            self.exploreConnectedComponent(i, marked, graph, i)
        
        connected_values_2_vertices = {}
        for [key, value] in marked.items():
            if value not in connected_values_2_vertices:
                connected_values_2_vertices[value] = [key]
            else:
                connected_values_2_vertices[value].append(key)
        
        connected_components = connected_values_2_vertices.values()
        
        result = array.copy()
        for connected_component in connected_components:
            # Sort with the lowest chars first
            indexes = connected_component.copy()
            indexes.sort()

            letters = connected_component.copy()
            letters.sort(key=lambda index: array[index])

        
            for index, letter in enumerate(letters):
                result[indexes[index]] = array[letter]
        
        return ''.join(result)
