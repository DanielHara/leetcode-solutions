# Question 1791: https://leetcode.com/problems/find-center-of-star-graph/

"""
    Easy, warm-up question
"""

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        vertex_index_to_number_edges = {}

        for [a, b] in edges:
            vertex_index_to_number_edges[a] = vertex_index_to_number_edges.get(a, 0) + 1
            vertex_index_to_number_edges[b] = vertex_index_to_number_edges.get(b, 0) + 1
        
        for [vertex, number_edges] in vertex_index_to_number_edges.items():
            if number_edges != 1:
                return vertex
