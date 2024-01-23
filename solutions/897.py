# Question 897: https://leetcode.com/problems/increasing-order-search-tree/

# Definitely not a difficult question






# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getInOrder(self, root: TreeNode) -> List[TreeNode]:
        if not root:
            return []

        return self.getInOrder(root.left) + [root] + self.getInOrder(root.right)
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes = self.getInOrder(root)

        for i in range(0, len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]

        nodes[-1].left = None
        nodes[-1].right = None

        return nodes[0]
