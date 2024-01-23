# Question 1572: https://leetcode.com/problems/matrix-diagonal-sum/

"""
    Very trivial question
"""

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0

        N = len(mat)

        for i in range(N):
            result = result + mat[i][i] + mat[N - i - 1][i]
        
        if N % 2 == 1:
            result = result - mat[N // 2][N // 2]
        
        return result
