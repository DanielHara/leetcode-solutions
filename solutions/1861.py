# Question 1861: https://leetcode.com/problems/rotating-the-box/

"""
    Just do it, not a difficult question
"""

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row_index, row in enumerate(box):
            i = 0

            while i < len(row):
                N_leaves = 0
                initial_i = i

                while i < len(row) and row[i] != '*':
                    if row[i] == '#':
                        N_leaves = N_leaves + 1
                    i = i + 1
                
                for k in range(initial_i, i - N_leaves):
                    box[row_index][k] = '.'
                for k in range(i - N_leaves, i):
                    box[row_index][k] = '#'
                
                i = i + 1
        
        # Now, rotate the matrix by 90
        M = len(box)
        N = len(box[0])

        result_matrix = [[None for i in range(M)] for j in range(N)]

        for row_index, row in enumerate(box):
            for column_index, element in enumerate(row):
                result_matrix[column_index][M - 1 - row_index] = element

        return result_matrix
