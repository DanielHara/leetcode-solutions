# Question 799: https://leetcode.com/problems/champagne-tower/

"""
    An amazingly interesting question! I had tried to solved this question a long time ago, but was overwhelmed.
    Just thought a bit about it today and the solution came easily. Just use a bit of DP and TADA!

    A way to further optimize this algorithm is probably based on the fact you don't have to calculate all the values in
    the tower, but just a few to answer the query.
"""

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [ [[None, None] for i in range(j + 1)] for j in range(query_row + 1)]

        dp[0][0] = [min(poured, 1), max(poured - 1, 0)]
        for row in range(1, query_row + 1):
            for col in range(row + 1):
                passed_1 = dp[row - 1][col - 1][1] / 2 if col >= 1 else 0
                passed_2 = dp[row - 1][col][1] / 2 if col <= row - 1 else 0
                passed = passed_1 + passed_2

                dp[row][col] = [min(passed, 1), max(passed - 1, 0)]

        return dp[query_row][query_glass][0]
