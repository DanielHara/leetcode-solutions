"""
Question 559: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

A rather trivial question, just go through the tree recursively and get the maximum height.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        depth = 0
        for child in root.children:
            depth = max(depth, self.maxDepth(child))
        
        return 1 + depth
