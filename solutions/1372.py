# Question 1372: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

"""
   Basically, this is just the naive approach, i.e, explore the whole tree and try to build zigzags starting with each node.
   However, you must use dynamic programming to save your previous results to avoid your solution to explode exponentially in time.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursiveExplore(self, root: Optional[TreeNode]):
        if not root:
            return
        
        self.recursiveLongestZigZag(root, True)
        self.recursiveLongestZigZag(root, False)
        
        self.recursiveExplore(root.left)
        self.recursiveExplore(root.right)
    
    def recursiveLongestZigZag(self, root: Optional[TreeNode], isRight: bool) -> int:
        if not root:
            return 0
        
        if isRight:
            if root.right is None:
                return 0
            
            if (id(root) in self.table) and 'right' in self.table[id(root)]:
                return self.table[id(root)]['right']
            
            result = self.recursiveLongestZigZag(root.right, False) + 1
            
            if id(root) not in self.table:
                self.table[id(root)] = {}
            self.table[id(root)]['right'] = result
            
            return result

        if root.left is None:
            return 0
        
        if (id(root) in self.table) and 'left' in self.table[id(root)]:
            return self.table[id(root)]['left']    
        
        result = self.recursiveLongestZigZag(root.left, True) + 1
        
        if id(root) not in self.table:
            self.table[id(root)] = {}
        self.table[id(root)]['left'] = result
        
        return result
    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.table = {}

        self.recursiveExplore(root)

        result = 0
        for value in self.table.values():
            for el in value.values():
                result = max(result, el)
        
        return result
