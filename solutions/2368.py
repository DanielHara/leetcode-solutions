# Question 2368: https://leetcode.com/problems/reachable-nodes-with-restrictions/

class Solution:
    def explore(self, start: int):
        if start in self.visited or start in self.restricted:
            return
        
        self.count = self.count + 1
        self.visited.add(start)

        for edge in self.reachable[start]:
            self.explore(edge)

    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        self.reachable = {}

        for edge in edges:
            if edge[0] not in self.reachable:
                self.reachable[edge[0]] = []
            
            self.reachable[edge[0]].append(edge[1])

            if edge[1] not in self.reachable:
                self.reachable[edge[1]] = []
            
            self.reachable[edge[1]].append(edge[0])
        
        self.restricted = set()
        for edge in restricted:
            self.restricted.add(edge)

        self.visited = set()
        self.count = 0

        self.explore(0)

        return self.count
