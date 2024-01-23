# Question 2319: https://leetcode.com/problems/check-if-matrix-is-x-matrix/

"""
    Just do it, trivial question
"""

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i == j or i + j == len(grid) - 1):
                    if grid[i][j] == 0:
                        return False
                else: 
                    if grid[i][j] != 0:
                        return False
                
        return True
