# Question 2685: https://leetcode.com/problems/count-the-number-of-complete-components/

"""
    Just do some DFS and see if each component is completely connected. No secrets, really
"""

class Solution:
    def recursiveExplore(self, start: int, from_to_edges, visited_set, connected_set):
        if start in visited_set:
            return
        
        connected_set.add(start)
        visited_set.add(start)

        for neighbor in from_to_edges.get(start, []):
            self.recursiveExplore(neighbor, from_to_edges, visited_set, connected_set)
    
    def isCompletelyConnected(self, connected_set, from_to_edges):
        connected_list = list(connected_set)
        for i in range(len(connected_list)):
            for j in range(i + 1, len(connected_list)):
                if connected_list[j] not in from_to_edges[connected_list[i]] or connected_list[i] not in from_to_edges[connected_list[j]]:
                    return False
        
        return True

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        from_to_edges = {}
        for [edge_a, edge_b] in edges:
            if edge_a not in from_to_edges:
                from_to_edges[edge_a] = []
            from_to_edges[edge_a].append(edge_b)
            
            if edge_b not in from_to_edges:
                from_to_edges[edge_b] = []
            from_to_edges[edge_b].append(edge_a)

        result = 0
        visited_set = set()
        for vertex in range(n):
            if vertex in visited_set:
                continue

            connected_set = set()
            self.recursiveExplore(vertex, from_to_edges, visited_set, connected_set)

            if self.isCompletelyConnected(connected_set, from_to_edges):
                result = result + 1

        return result
            
