"""
    Question 2596: https://leetcode.com/problems/check-knight-tour-configuration/

    Trivial question, just do it
"""

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False

        number_rows = len(grid)
        number_cols = len(grid[0])

        location = [0, 0]
        step = 1
        while step < number_rows * number_cols:
            [x, y] = location
            points = [[x + 2, y + 1], [x + 1, y + 2], [x - 2, y + 1], [x - 1, y + 2], [x + 2, y - 1], [x + 1, y - 2], [x - 2, y - 1], [x - 1, y - 2]]

            found = False
            for point in points:
                [row, col] = point

                if row >= 0 and row < number_rows and col >= 0 and col < number_cols and grid[row][col] == step:
                    location = [row, col]
                    step = step + 1
                    found = True
                    continue
            
            if not found:
                return False
        
        return True
