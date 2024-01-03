"""
    Question 629: https://leetcode.com/problems/k-inverse-pairs-array/description/

    A very interesting question, I just used some DP. Make S[i][j] the number of different arrays from 1 to n and
    a number of inversions less or equal to j.
"""

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if n <= 1:
            return 0 if k > 0 else 1

        if k == 0:
            return 1

        mod = 10**9 + 7

        S = [[0 for i in range(k + 1)] for j in range(n + 1)]
        S[2][0] = 1
        S[2][1] = 2
        
        for i in range(2, k + 1, 1):
            S[2][i] = 2

        for i in range(2, n):
            for j in range(0, k + 1):
                total = S[i + 1][j - 1] if j > 0 else 0

                total = total + S[i][j]
                
                if j - i - 1 >= 0:
                    total = total - S[i][j - i - 1]
                
                S[i + 1][j] = total

        return (S[n][k] - S[n][k - 1]) % mod
