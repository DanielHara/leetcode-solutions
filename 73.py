"""
    Question 73: https://leetcode.com/problems/set-matrix-zeroes/

    This presents a O(N**3) solution in procession time, and O(1) in space.
    Not a difficult solution to devise.
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for col in range(n):
                        if col != j and matrix[i][col] != 0:
                            matrix[i][col] = None
                    
                    for row in range(m):
                        if row != i and matrix[row][j] != 0:
                            matrix[row][j] = None
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == None:
                    matrix[i][j] = 0

