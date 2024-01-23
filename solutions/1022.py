"""
Question 1022: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/submissions/

Just do it!
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getBinaries(self, root: Optional[TreeNode]):
        if not root:
            return []

        left = self.getBinaries(root.left)
        right = self.getBinaries(root.right)

        if not root.left and not root.right:
            return [[root.val]]

        result = []
        for el in left:
            el.append(root.val)
            result.append(el)
        
        for el in right:
            el.append(root.val)
            result.append(el)
        
        return result


    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        binaries = self.getBinaries(root)

        result = 0
        for stack in binaries:
            while stack:
                el = stack.pop()
                result = result + el * 2 ** (len(stack))
        
        return result

