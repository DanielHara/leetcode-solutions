# Question 797: https://leetcode.com/problems/all-paths-from-source-to-target/

"""
    Just do simple DFS.
"""


class Solution:
    def DFS(self, graph, origin, previous_path, destination):
        if origin == destination:
            return [[destination]]

        neighbors = graph[origin]
        result = []
        for neighbor in neighbors:
            paths = self.DFS(graph, neighbor, previous_path + [origin], destination)
            for path in paths:
                result.append([origin] + path)

        return result

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)

        return self.DFS(graph, 0, [], n - 1)
