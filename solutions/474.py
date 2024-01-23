"""
Question 474: https://leetcode.com/problems/ones-and-zeroes/description/

Very interesting question. It's a version of the Knapsack problem: https://en.wikipedia.org/wiki/Knapsack_problem

I got the answer by remembering what I did a long time ago: https://github.com/DanielHara/SubSetProblem
"""

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        S_length = len(strs)

        dp = [[[0 for i in range(n + 1)] for j in range(m + 1)] for k in range(S_length)]

        # dp[i][j][k] is the size of the largest subset which considers strs[i].
        # If there's no such subset, it's 0

        frequencies = []
        for string in strs:
            frequency = [0, 0]
            for char in string:
                if char == '0':
                    frequency[0] = frequency[0] + 1
                else:
                    frequency[1] = frequency[1] + 1
            frequencies.append(frequency)
        
        # Initialization:
        for j in range(m + 1):
            for k in range(n + 1):
                dp[0][j][k] = 1 if (frequencies[0][0] <= j and frequencies[0][1] <= k) else 0

        for i in range(1, S_length):
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k])
                    
                    [number_zeros, number_ones] = frequencies[i]
                    if j - number_zeros < 0 or k - number_ones < 0:
                        continue
                    
                    candidate = dp[i - 1][j - number_zeros][k - number_ones]
                    dp[i][j][k] = max(dp[i][j][k], 1 + candidate)

        return max(dp[S_length - 1][m][n], 0)
