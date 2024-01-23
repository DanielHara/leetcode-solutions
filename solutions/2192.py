# Question 2192: https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph

"""
    A very interesting question! Just use a bit of DP for the solution not to explode in time

    When I started to solve it, I mixed up ancestor and descendents, and it messed up my code a bit :/
"""

class Solution:
    def exploreGraph(self, start: int, from_to_dictionary):
        if start in self.ancestors_dict:
            return self.ancestors_dict[start]

        result = set()
        for to_node in from_to_dictionary.get(start, []):
            result.add(to_node)

            descendents = self.exploreGraph(to_node, from_to_dictionary)
            for node in descendents:
                result.add(node)
            
        self.ancestors_dict[start] = result
        return result

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        from_to_dictionary = {}
        for [from_node, to_node] in edges:
            if to_node not in from_to_dictionary:
                from_to_dictionary[to_node] = []
            from_to_dictionary[to_node].append(from_node)

        self.ancestors_dict = {}
        for i in range(n):
            self.exploreGraph(i, from_to_dictionary)
        
        result = []
        for i in range(n):
            result.append([])

        for i in range(n):
            descendents = list(self.ancestors_dict.get(i, []))
            descendents.sort()

            result[i] = descendents

        return result
