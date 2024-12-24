# Question 2684: https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

"""
    Just use some DP, really no secret.
"""

class Solution:
    # Gives you tha maximum number of moves starting from cell [start_row, start_col]
    def recursiveMaxMoves(self, start_row: int, start_col: int) -> int:
        if self.dp[start_row][start_col] is not None:
            return self.dp[start_row][start_col]

        result = 0

        number_rows = len(self.grid)
        number_cols = len(self.grid[0])

        possible_moves = [[start_row - 1, start_col + 1], [start_row, start_col + 1], [start_row + 1, start_col + 1]]
        for [row, col] in possible_moves:
            if row >= 0 and row < number_rows and col >= 0 and col < number_cols and self.grid[row][col] > self.grid[start_row][start_col]:
                result = max(result, 1 + self.recursiveMaxMoves(row, col))
        
        self.dp[start_row][start_col] = result
        return result

    def maxMoves(self, grid: List[List[int]]) -> int:
        self.grid = grid

        number_rows = len(self.grid)
        number_cols = len(self.grid[0])

        self.dp = [[None for col in range(number_cols)] for row in range(number_rows)]
        
        result = 0
        for row in range(number_rows):
            result = max(result, self.recursiveMaxMoves(row, 0))
        
        return result
