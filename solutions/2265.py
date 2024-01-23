# Question 2265: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

"""
    Quite a simple question, solvable with recursion (CS 101).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def exploreTree(self, root: TreeNode):
        if not root:
            return 0, 0, 0

        (left_sum_values_of_children, number_of_left_children, result_left) = self.exploreTree(root.left)
        (right_sum_values_of_children, number_of_right_children, result_right) = self.exploreTree(root.right)

        number_of_children = 1 + number_of_left_children + number_of_right_children

        sum_values_of_children = root.val + left_sum_values_of_children + right_sum_values_of_children

        return sum_values_of_children, number_of_children, result_left + result_right + (1 if sum_values_of_children // number_of_children == root.val else 0)
    
    def averageOfSubtree(self, root: TreeNode) -> int:
        exploredTree = self.exploreTree(root)

        return exploredTree[2]
