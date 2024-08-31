"""
    Question 2477:https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

    Do Breadth First Search twice:
    Once to find the number of representatives in each node, and another one to calculate the result.
"""

import math

class Solution:
    # Start with node_index_to_number_representatives = {}
    # visited = set()
    def findNumberRepresentatives(self, start, from_to_dict, visited, node_index_to_number_representatives):
        if start in visited:
            return 0
        
        visited.add(start)

        result = 1
        neighbours = from_to_dict.get(start, [])
        for neighbour in neighbours:
            result = result + self.findNumberRepresentatives(neighbour, from_to_dict, visited, node_index_to_number_representatives)

        node_index_to_number_representatives[start] = result
        return result


    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # You can solve this breadth-first search
        from_to_dict = {}
        for road in roads:
            if road[0] not in from_to_dict:
                from_to_dict[road[0]] = []
            from_to_dict[road[0]].append(road[1])

            if road[1] not in from_to_dict:
                from_to_dict[road[1]] = []
            from_to_dict[road[1]].append(road[0])
        
        node_index_to_number_representatives = {}
        self.findNumberRepresentatives(0, from_to_dict, set(), node_index_to_number_representatives)
        
        result = 0
        
        border = [0]
        visited = set()
        while border:
            new_border = []
            while border:
                node = border.pop()
                if node in visited:
                    continue
                
                visited.add(node)
                neighbours = from_to_dict.get(node, [])

                for neighbour in neighbours:
                    if neighbour not in visited:
                        fuel = math.ceil(node_index_to_number_representatives[neighbour] / seats)
                        result = result + fuel
                        new_border.append(neighbour)
            border = new_border

        return result
        
