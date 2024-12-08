# Question 2326: https://leetcode.com/problems/spiral-matrix-iv/

"""
    This question is quite simple, but very interesting!
"""

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for col in range(n)] for row in range(m)]

        row = 0
        col = 0
        p = head
        while p:
            # Go right
            while p and col < n - 1 and matrix[row][col + 1] == -1:
                matrix[row][col] = p.val
                col = col + 1
                p = p.next
            # Go down
            while p and row < m - 1 and matrix[row + 1][col] == -1:
                matrix[row][col] = p.val
                row = row + 1
                p = p.next
            # Go left
            while p and col >= 1 and matrix[row][col - 1] == -1:
                matrix[row][col] = p.val
                col = col - 1
                p = p.next
            # Go up
            while p and row >= 1 and matrix[row - 1][col] == -1:
                matrix[row][col] = p.val
                row = row - 1
                p = p.next
            
            if p and p.next is None:
                matrix[row][col] = p.val
                p = p.next

        return matrix
