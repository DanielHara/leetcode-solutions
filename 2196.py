# Question 2196: https://leetcode.com/problems/create-binary-tree-from-descriptions/

# The problem really gives a hint that you could use a hash table to store which are the left and right nodes,
# as the values of the binary tree are unique. You could do so storing a new node if you've never seen a value before.
# A node without a parent is the root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        table = {}
        
        for description in descriptions:
            [parent, child, isLeft] = description
            
            if parent not in table:
                table[parent] = {
                    'left': None,
                    'right': None,
                    'parent': None,
                    'node': TreeNode(parent)
                }
            
            if isLeft:
                table[parent]['left'] = child
            else:
                table[parent]['right'] = child
            
            if child not in table:
                table[child] = {
                    'left': None,
                    'right': None,
                    'parent': None,
                    'node': TreeNode(child)
                }
            
            table[child]['parent'] = parent
        
        root = None
        
        for key in table:
            node = table[key]['node']
            if table[key]['parent'] is None:
                root = node
            
            left = table[key]['left']
            if left is not None:
                node.left = table[left]['node']
            
            right = table[key]['right']
            if right is not None:
                node.right = table[right]['node']
        
        return root
