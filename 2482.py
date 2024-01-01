"""
Question 2482: https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

    Another easy question labelled as Medium. Just do it, no secrets, no tricks.
"""


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        onesRow = [0 for i in range(m)]
        onesCol = [0 for i in range(n)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    onesRow[row] = onesRow[row] + 1
                    onesCol[col] = onesCol[col] + 1
        
        result = [[0 for i in range(n)] for j in range(m)]

        for row in range(m):
            for col in range(n):
                result[row][col] = onesRow[row] - (n - onesRow[row]) + onesCol[col] - (m - onesCol[col])

        return result
