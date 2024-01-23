# Question 1584: https://leetcode.com/problems/min-cost-to-connect-all-points/

"""
Use Kruskal algorithm: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm, and use 
a UnionFind data structure to find out which nodes are in the same tree.
"""

class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0 for _ in self.parents]
    
    def union(self, x, y):
        i = self.find(x)
        j = self.find(y)
        if i != j:
            if self.ranks[i] < self.ranks[j]:
                self.parents[i] = j
            elif self.ranks[j] < self.ranks[i]:
                self.parents[j] = i
            else:
                self.parents[j] = i
                self.ranks[i] += 1
    
    def find(self, x):
        if x == self.parents[x]:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    
class Solution:
    # Kruskal algorithm:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        
        union_find = UnionFind(N)
        
        heap = []
        for i in range(N):
            for j in range(i + 1, N):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                
                heapq.heappush(heap, (dist, (i, j)))
        
        result = 0
        while heap:
            el = heapq.heappop(heap)
            dist = el[0]
            (i, j) = el[1]
        
            if union_find.find(i) != union_find.find(j):
                result = result + dist
                union_find.union(i, j)
        
        return result
