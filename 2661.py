# Question 2661: https://leetcode.com/problems/first-completely-painted-row-or-column/

# A quite easy question, actually. Just use some maps.

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        integer_2_matrix_position = {}

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                integer_2_matrix_position[mat[i][j]] = [i, j]
        
        column_map = {}
        row_map = {}

        for index, number in enumerate(arr):
            [row, column] = integer_2_matrix_position[number]

            row_map[row] = row_map.get(row, 0) + 1
            if row_map[row] == len(mat[0]):
                return index
            
            column_map[column] = column_map.get(column, 0) + 1
            if column_map[column] == len(mat):
                return index
