# Question 419: https://leetcode.com/problems/battleships-in-a-board/

"""
    This is a very interesting question! I dived directly into the follow-up:
        Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?
    Just be carefully about counting the battleships twice, and that's it.
"""

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        number_rows = len(board)
        number_cols = len(board[0])
        
        doubly_counted_battleships = 0

        result = 0
        # See only horizontally laid battleships
        for row in range(number_rows):
            col = 0
            while col < number_cols:
                while col < number_cols and board[row][col] == '.':
                    col = col + 1
                
                if col < number_cols:
                    result = result + 1
                
                if col == number_cols - 1 or (col < number_cols and board[row][col + 1] == '.'):
                    doubly_counted_battleships = doubly_counted_battleships + 1

                while col < number_cols and board[row][col] == 'X':
                    col = col + 1
        
        # See only vertically laid battleships
        for col in range(number_cols):
            row = 0
            while row < number_rows:
                while row < number_rows and board[row][col] == '.':
                    row = row + 1
                
                if row < number_rows:
                    result = result + 1
                
                if row == number_rows - 1 or (row < number_rows and board[row + 1][col] == '.'):
                    doubly_counted_battleships = doubly_counted_battleships + 1
                
                while row < number_rows and board[row][col] == 'X':
                    row = row + 1
        
        single_cell_battleships = 0
        for row in range(number_rows):
            for col in range(number_cols):
                if (row == 0 or board[row - 1][col] == '.') and (row == number_rows - 1 or board[row + 1][col] == '.') and (col == 0 or board[row][col - 1] == '.') and (col == number_cols - 1 or board[row][col + 1] == '.') and board[row][col] == 'X':
                    single_cell_battleships = single_cell_battleships + 1

        return result - doubly_counted_battleships + single_cell_battleships
