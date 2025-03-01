# Question 2075: https://leetcode.com/problems/decode-the-slanted-ciphertext/

"""
    Just do it, no secrets, no optimization, nothing
"""

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        matrix = [[' ' for col in range(cols)] for row in range(rows)]

        for index, char in enumerate(encodedText):
            matrix[index // cols][index % cols] = char

        tokens = []
        for start_col in range(0, cols, 1):
            for row in range(rows):
                if row + start_col < cols:
                    tokens.append(matrix[row][row + start_col])
                else:
                    break
        
        while tokens and tokens[-1] == ' ':
            tokens.pop()

        return ''.join(tokens)
