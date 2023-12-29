"""
Question 2428: https://leetcode.com/problems/maximum-sum-of-an-hourglass/

    No idea why this question is rated as Medium. Should be Easy. Or even not be on Leetcode at all, as it's trivial.
"""

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        # grid is a N x M matrix:
        N = len(grid)
        M = len(grid[0])

        result = 0
        for row in range(1, N - 1):
            for col in range(1, M - 1):
                s = grid[row][col] + grid[row - 1][col - 1] + grid[row - 1][col] + grid[row - 1][col + 1] + grid[row + 1][col - 1] + grid[row + 1][col] + grid[row + 1][col + 1]

                result = max(result, s)
        
        return result
