"""
Question 938: https://leetcode.com/problems/range-sum-of-bst/

A fairly easy question. Explore the tree recursively. If you find a root whose value is lower than low, maybe the tree with
root.right still contains elements >= low, and analogously for the case where the root has a value higher than high.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        if root.val >= low and root.val <= high:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        
        
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        
        return self.rangeSumBST(root.left, low, high)
        
        