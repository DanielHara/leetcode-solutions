"""
Question 2096: https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

Explore the tree and find the paths to startValue and destValue. Then, compare the paths to get the answer

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Returns None if target not in root
    def findDirectionsToNode(self, root: Optional[TreeNode], target):
        if not root:
            return None
        
        if root.val == target:
            return []
        
        left = self.findDirectionsToNode(root.left, target)
        
        if left is not None:
            left.append('L')
            return left
        
        right = self.findDirectionsToNode(root.right, target)
        
        if right is not None:
            right.append('R')
            return right
        
        return None
    
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # First, find both nodes:
        
        startPath = self.findDirectionsToNode(root, startValue)
        destPath = self.findDirectionsToNode(root, destValue)
        
        while startPath and destPath and startPath[-1] == destPath[-1]:
            startPath.pop()
            destPath.pop()
        
        if startPath:
            array = ['U' for i in range(len(startPath))] + list(reversed(destPath))
            return ''.join(array)
        
        return ''.join(list(reversed(destPath)))
