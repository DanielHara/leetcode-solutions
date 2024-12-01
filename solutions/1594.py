# Question 1594: https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

"""
    Just use some DP, and save the highest and lowest possible product for each position in the matrix.
"""

class Solution:
    def recursiveMaxProductPath(self, grid, start):
        number_rows = len(grid)
        number_cols = len(grid[0])

        [start_row, start_col] = start

        if self.dp[start_row][start_col] is not None:
            return self.dp[start_row][start_col]

        if start_row == number_rows - 1 and start_col == number_cols - 1:
            self.dp[start_row][start_col] = [grid[start_row][start_col]]
            return [grid[start_row][start_col]]
        
        options = []
        if start_row < number_rows - 1:
            options = options + self.recursiveMaxProductPath(grid, [start_row + 1, start_col])
        
        if start_col < number_cols - 1:
            options = options + self.recursiveMaxProductPath(grid, [start_row, start_col + 1])

        element = grid[start_row][start_col]
        possibilities = []
        for option in options:
            possibilities.append(option * element)
        
        possibilities.sort()
        result = [possibilities[0], possibilities[-1]]
        
        self.dp[start_row][start_col] = result
        return result

    # Just try brute-force
    def maxProductPath(self, grid: List[List[int]]) -> int:
        number_rows = len(grid)
        number_cols = len(grid[0])
        self.dp = [[None for col in range(number_cols)] for row in range(number_rows)]

        self.recursiveMaxProductPath(grid, [0, 0])

        maximum = max(self.dp[0][0])
        
        return maximum % (10**9 + 7) if maximum >= 0 else -1

