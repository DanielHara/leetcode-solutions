# Question 2385: https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/

"""
    An extraordinarily interesting question, which only seems quite easy! However, writing the code for it wasn't that
    straightforward to me.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def exploreTree(self, root: Optional[TreeNode], start: int):
        if not root:
            return

        if root.val == start:
            self.start_node = root

        self.node_to_height[root.val] = 1
        
        if root.left:
            self.node_to_parent[root.left.val] = root
            self.exploreTree(root.left, start)
            self.node_to_height[root.val] = max(self.node_to_height[root.val], 1 + self.node_to_height[root.left.val])

        if root.right:
            self.node_to_parent[root.right.val] = root
            self.exploreTree(root.right, start)
            self.node_to_height[root.val] = max(self.node_to_height[root.val], 1 + self.node_to_height[root.right.val])
    
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.start_node = None

        self.node_to_parent = {}
        self.node_to_height = {}

        self.exploreTree(root, start)

        start_node = self.start_node

        result = self.node_to_height[start_node.left.val] if start_node.left else 0
        result = max(result, self.node_to_height[start_node.right.val] if start_node.right else 0)

        ant_p = start_node
        p = self.node_to_parent.get(start_node.val, None)
        count = 1
        while p:
            if self.node_to_parent.get(p.val, None) is None:
                result = max(result, count)

            if p.left:
                if p.left.val != ant_p.val:
                    result = max(result, count + self.node_to_height[p.left.val])
                else:
                    result = max(result, count - 1)
            if p.right:
                if p.right.val != ant_p.val:
                    result = max(result, count + self.node_to_height[p.right.val])
                else:
                    result = max(result, count - 1)

            ant_p = p
            p = self.node_to_parent.get(p.val, None)
            count = count + 1
        
        return result
