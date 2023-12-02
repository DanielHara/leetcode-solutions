# Question 2316: https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

"""
    Quite interesting question! Just explore the graph, and use a simple trick to calculate the pairs between the fully-connected regions.
"""

class Solution:
    def countNumberOfNodesInRegion(self, start: int, edges_dict, visited) -> int:
        if start in visited:
            return 0
        
        visited.add(start)
        result = 1

        for neighbor in edges_dict.get(start, []):
            result = result + self.countNumberOfNodesInRegion(neighbor, edges_dict, visited)
        
        return result

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        edges_dict = {}

        for [u, v] in edges:
            if u not in edges_dict:
                edges_dict[u] = set()
            edges_dict[u].add(v)

            if v not in edges_dict:
                edges_dict[v] = set()
            edges_dict[v].add(u)
        
        
        visited = set()

        regions_counts = []
        for node in range(n):
            if node in visited:
                continue

            node_count_in_new_region = self.countNumberOfNodesInRegion(node, edges_dict, visited)
            regions_counts.append(node_count_in_new_region)

        result = 0
        total_sum = sum(regions_counts)
        for i in range(len(regions_counts)):
            result = result + (total_sum - regions_counts[i]) * regions_counts[i]

        return result // 2
