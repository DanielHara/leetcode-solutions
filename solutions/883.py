# Question 883: https://leetcode.com/problems/projection-area-of-3d-shapes/

"""
    Interesting easy question
"""

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        x_projection = 0
        y_projection = 0
        z_projection = 0

        maximum_columns = [0 for i in range(len(grid[0]))]
        for i in range(len(grid)):
            maximum_line = 0
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    x_projection = x_projection + 1
                maximum_line = max(maximum_line, grid[i][j])
                maximum_columns[j] = max(maximum_columns[j], grid[i][j])
            
            y_projection = y_projection + maximum_line
        
        z_projection = sum(maximum_columns)

        return x_projection + y_projection + z_projection
