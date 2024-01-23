# Question 2359: https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

"""
    Interesting question, nothing fancy. Just do it
"""

class Solution:
    # Just explore the graph from start and return an array with the distances. Use breadth-first search
    def getDistancesFromNode(self, edges: List[int], start: int):
        result_array = [-1 for i in range(len(edges))]

        border = [start]

        distance = 0
        visited = set()
        while border:
            new_border = []

            while border:
                node = border.pop()
                if node in visited:
                    continue

                visited.add(node)

                result_array[node] = distance
                
                if edges[node] != -1:
                    new_border.append(edges[node])
            
            border = new_border
            distance = distance + 1

        return result_array
    
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        distance_array1 = self.getDistancesFromNode(edges, node1)
        distance_array2 = self.getDistancesFromNode(edges, node2)

        result_node = -1
        for node in range(len(edges)):
            distance1 = distance_array1[node]
            distance2 = distance_array2[node]

            if distance1 >= 0 and distance2 >= 0:
                if result_node == -1:
                    result_node = node
                elif max(distance1, distance2) < max(distance_array1[result_node], distance_array2[result_node]):
                    result_node = node
        
        return result_node
