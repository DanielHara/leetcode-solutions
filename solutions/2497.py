"""
    Question 2497: https://leetcode.com/problems/maximum-star-sum-of-a-graph/

    Just create a dictionary, where the keys are node_index, and the value is a heap, where you store the values of the neighbours of the node node_index.
    They just pop k values, and get the optimal node.
"""

import heapq

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        node_index_to_neighbours = {}

        for [a, b] in edges:
            if a not in node_index_to_neighbours:
                node_index_to_neighbours[a] = []
            heapq.heappush(node_index_to_neighbours[a], (-vals[b], vals[b]))

            if b not in node_index_to_neighbours:
                node_index_to_neighbours[b] = []
            heapq.heappush(node_index_to_neighbours[b], (-vals[a], vals[a]))

        result = vals[0]
        for node_index in range(len(vals)):
            neighbours = node_index_to_neighbours.get(node_index, [])

            s = vals[node_index]
            for count in range(k):
                if not neighbours:
                    break
                popped_element = heapq.heappop(neighbours)
                value = popped_element[1]
                if value <= 0:
                    break

                s = s + value

            result = max(result, s)
        
        return result
