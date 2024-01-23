# Question 2374: https://leetcode.com/problems/node-with-highest-edge-score/

"""
    Quite easy question, just a bit of manipulation.
"""


from functools import cmp_to_key

class Solution:
    def comparison(self, item1, item2):
        if item1[1] < item2[1]:
            return 1
        
        if item1[1] > item2[1]:
            return -1

        if item1[0] < item2[0]:
            return -1
        
        if item1[1] > item2[0]:
            return 1

        return 0


    def edgeScore(self, edges: List[int]) -> int:
        node_2_number_of_incoming_edges = {}

        for index, edge in enumerate(edges):
            node_2_number_of_incoming_edges[edges[index]] = node_2_number_of_incoming_edges.get(edges[index], 0) + index
        
        items = list(node_2_number_of_incoming_edges.items())

        items.sort(key=cmp_to_key(self.comparison))

        return items[0][0]
