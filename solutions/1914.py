# Question 1914: https://leetcode.com/problems/cyclically-rotating-a-grid/

"""
  Just store the layers in an array, and do the rotation. Nothing fancy.
  O(n * m) processing time
"""

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        number_rows = len(grid)
        number_cols = len(grid[0])

        left_border = 0
        top_border = 0
        right_border = number_cols - 1
        bottom_border = number_rows - 1

        while left_border < right_border and top_border < bottom_border:
            temp_array = []
            for col in range(left_border, right_border + 1):
                temp_array.append(grid[top_border][col])
            for row in range(top_border + 1, bottom_border + 1):
                temp_array.append(grid[row][right_border])
            for col in range(right_border - 1, left_border - 1, -1):
                temp_array.append(grid[bottom_border][col])
            for row in range(bottom_border - 1, top_border, -1):
                temp_array.append(grid[row][left_border])

            index = 0
            for col in range(left_border, right_border + 1):
                grid[top_border][col] = temp_array[(index + k) % len(temp_array)]
                index = index + 1

            for row in range(top_border + 1, bottom_border + 1):
                grid[row][right_border] = temp_array[(index + k) % len(temp_array)]
                index = index + 1

            for col in range(right_border - 1, left_border - 1, -1):
                grid[bottom_border][col] = temp_array[(index + k) % len(temp_array)]
                index = index + 1

            for row in range(bottom_border - 1, top_border, -1):
                grid[row][left_border] = temp_array[(index + k) % len(temp_array)]
                index = index + 1

            left_border = left_border + 1
            right_border = right_border - 1
            top_border = top_border + 1
            bottom_border = bottom_border - 1
        
        return grid
