# Question 2039: https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

"""
    Very interesting question.
    Just do breadth-first search to know the distance between each server and the master server, and 
    use some math.
"""

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        edges_dict = {}

        for [u, v] in edges:
            if u not in edges_dict:
                edges_dict[u] = []
            if v not in edges_dict:
                edges_dict[v] = []
            edges_dict[u].append(v)
            edges_dict[v].append(u)

        # Breadth-first search:
        borders = [0]
        distance = 0
        min_distance_dict = {}
        
        while borders:
            new_borders = []
            while borders:
                el = borders.pop()
                if el in min_distance_dict:
                    continue
                min_distance_dict[el] = distance
                for v in edges_dict.get(el, []):
                    new_borders.append(v)
            distance = distance + 1
            borders = new_borders
        
        result = 1
        for i in range(1, len(patience)):
            distance = min_distance_dict[i]

            p = patience[i]
            if (2 * distance) % p != 0:
                n = (2 * distance) // p
            else:
                n = (2 * distance) // p - 1

            result = max(result, 1 + 2 * distance + n * p)
        
        return result
