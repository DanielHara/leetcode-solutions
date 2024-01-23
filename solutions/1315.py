# Question 1315: https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

"""
    Doing it recursively is very easy
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 0
        
        result = 0
        if root.val % 2 == 0:
            if root.left:
                if root.left.left:
                    result = result + root.left.left.val
                
                if root.left.right:
                    result = result + root.left.right.val

            if root.right:
                if root.right.left:
                    result = result + root.right.left.val
            
                if root.right.right:
                    result = result + root.right.right.val
        
        result = result + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)

        return result
