# Question 987: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

"""
    A very straightforward question. Just use a hash map, nothing difficult.
    This question should actually be labaled as Medium
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, root: Optional[TreeNode], row: int, col: int):
        if not root:
            return

        self.min_column = min(self.min_column, col)
        self.max_column = max(self.max_column, col)
        self.max_row = max(self.max_row, row)
        
        key = str(row) + '_' + str(col)
        if key not in self.col_row_to_array_dict:
            self.col_row_to_array_dict[key] = []

        self.col_row_to_array_dict[key].append(root.val)
        self.DFS(root.left, row + 1, col - 1)
        self.DFS(root.right, row + 1, col + 1)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        self.col_row_to_array_dict = {}

        self.min_column = 0
        self.max_column = 0
        self.max_row = 0

        self.DFS(root, 0, 0)

        result = []

        for col in range(self.min_column, self.max_column + 1, 1):
            vertical = []

            for row in range(0, self.max_row + 1, 1):
                key = str(row) + '_' + str(col)
                if key in self.col_row_to_array_dict:
                    vertical = vertical + sorted(self.col_row_to_array_dict[key])

            result.append(vertical)

        return result
