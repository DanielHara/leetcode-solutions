# Question 1992: https://leetcode.com/problems/find-all-groups-of-farmland/

"""
    Simply explore the grid and transform the rectangles you find in 0s so that you don't count
    them twice.
"""

class Solution:
    def explore(self, start: List[int], land: List[List[int]]):
        n = len(land)
        m = len(land[0])

        [i, j] = start
        
        if land[i][j] == 0:
            return None
        
        p = i
        q = j
        while p + 1 < n and land[p + 1][q] == 1:
            p = p + 1
        
        while q + 1 < m and land[p][q + 1] == 1:
            q = q + 1
        
        for r in range(i, p + 1):
            for s in range(j, q + 1):
                land[r][s] = 0
        
        return [i, j, p, q]

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # land has n lines and m columns:
        
        n = len(land)
        m = len(land[0])
        
        result = []
        for i in range(n):
            for j in range(m):
                el = self.explore([i, j], land)
                if el is not None:
                    result.append(el)
        
        return result
