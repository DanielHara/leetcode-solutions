"""
Question 671: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
"""

"""
Trivial question, just do it!
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Returns the value of the first node it find thats is > threshold, and None if it doesn't find anything
    def explore(self, root: Optional[TreeNode], threshold: int) -> int:
        if not root:
            return None
        
        if root.val > threshold:
            return root.val
        
        if root.left and root.right:
            left = self.explore(root.left, threshold)
            right = self.explore(root.right, threshold)
            
            if left is not None and right is not None:
                return min(left, right)
            
            if left is not None:
                return left
            
            if right is not None:
                return right
        
        return None
    
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        left = self.explore(root.left, root.val)
        right = self.explore(root.right, root.val)
        
        if left is not None and right is not None:
            return min(left, right)
            
        if left is not None:
            return left
            
        if right is not None:
            return right
        
        return -1
