# Question 872: https://leetcode.com/problems/leaf-similar-trees/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeaves(self, root: Optional[TreeNode]) -> [TreeNode]:
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        if root.left and root.right:
            return self.getLeaves(root.left) + self.getLeaves(root.right)
        
        if root.left:
            return self.getLeaves(root.left)
        
        return self.getLeaves(root.right)
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = self.getLeaves(root1)
        leaves2 = self.getLeaves(root2)

        return leaves1 == leaves2
