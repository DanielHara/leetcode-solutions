"""
Question 1504: https://leetcode.com/problems/count-submatrices-with-all-ones/

    Very interesting question! I just use a bit of a DP-trick to get a O(N*3) solution, where N = max(m, n)
    A brutal-force solution would be O(N*4), and probably won't pass the judge.
"""

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        N = len(mat)
        M = len(mat[0])

        distance_to_first_zero_matrix = [[0 for j in range(M)] for i in range(N)]

        result = 0
        for row in range(N - 1, -1, -1):
            for col in range(M - 1, -1, -1):
                if mat[row][col] == 0:
                    distance_to_first_zero_matrix[row][col] = 0
                else:
                    if row + 1 < N:
                        distance_to_first_zero_matrix[row][col] = 1 + distance_to_first_zero_matrix[row + 1][col]
                    else:
                        distance_to_first_zero_matrix[row][col] = 1
        
        result = 0
        for row in range(N - 1, -1, -1):
            for col in range(M - 1, -1, -1):
                height = distance_to_first_zero_matrix[row][col]

                col_index = col
                while col_index < M and mat[row][col_index] == 1:
                    height = min(height, distance_to_first_zero_matrix[row][col_index])
                    result = result + height

                    col_index = col_index + 1
        return result
