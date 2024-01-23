# Question 1812: https://leetcode.com/problems/determine-color-of-a-chessboard-square/

"""
    Very trivial question, no explanation really needed.
"""

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        column = ord(coordinates[0]) - ord('a')
        row = int(coordinates[1]) - 1
        
        return (row % 2 == 1 and column % 2 == 0) or (row % 2 == 0 and column % 2 == 1)
