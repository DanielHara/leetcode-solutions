# Question 1905: https://leetcode.com/problems/count-sub-islands/

"""
Simply depth-explore each island in grid2, checking if the corresponding position is also 1 in grid1.
After exploring a point with value 1 in grid2, keep the exploration to mark them as visited (or simply turn them into water),
in order to avoid an infinite loop or counting a sub-island twice.
"""
class Solution:
    # Supposes grid2[i][j] = 1
    def isSubIsland(self, i: int, j: int, grid1: List[List[int]], grid2: List[List[int]]):
        if grid1[i][j] == 0:
            return False
        
        grid2[i][j] = 0
        
        possibilities = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
        
        result = True
        for possibility in possibilities:
            [p, q] = possibility
            
            if p >= 0 and p < len(grid1) and q >= 0 and q < len(grid1[0]) and grid2[p][q] == 1:
                if not self.isSubIsland(p, q, grid1, grid2):
                    result = False
        return result
    
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # grid2 has n lines and m columns
        n = len(grid2)
        m = len(grid2[0])
        
        result = 0
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1 and self.isSubIsland(i, j, grid1, grid2):
                    result = result + 1
        
        return result

