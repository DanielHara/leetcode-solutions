# Question 661: https://leetcode.com/problems/image-smoother/

"""
    Easy, but interesting question! It reminds me of the chapters I'm reading on machine learning and Image Processing.
"""

class Solution:
    def getAverage(self, img: List[List[int]], row: int, col: int):
        number_rows = len(img)
        number_columns = len(img[0])

        cells = []
        for cell_row in range(max(row - 1, 0), min(row + 1, number_rows - 1) + 1):
            for cell_column in range(max(col - 1, 0), min(col + 1, number_columns - 1) + 1):
                cells.append(img[cell_row][cell_column])

        return sum(cells) // len(cells)

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        number_rows = len(img)
        number_columns = len(img[0])

        answer = [[None for col in range(number_columns)] for row in range(number_rows)]
        for row in range(number_rows):
            for col in range(number_columns):
                answer[row][col] = self.getAverage(img, row, col)

        return answer

