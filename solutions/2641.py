# Question 2641: https://leetcode.com/problems/cousins-in-binary-tree-ii/

"""
    Just use a map to keep track to the sum of the values of a node and its sibling (if any), and go through the tree
    in depth-level, as usual.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        child_to_parent_value_sum = {}

        queue = [root, None]

        while len(queue) > 1:
            total = 0
            nodes_in_level = []

            while queue and queue[0] != None:
                node = queue.pop(0)
                nodes_in_level.append(node)
                total = total + node.val

                left = node.left
                right = node.right
                parent_value_sum = 0
                if left:
                    parent_value_sum = parent_value_sum + left.val
                    queue.append(left)
                if right:
                    parent_value_sum = parent_value_sum + right.val
                    queue.append(right)
                
                if left:
                    child_to_parent_value_sum[id(left)] = parent_value_sum
                if right:
                    child_to_parent_value_sum[id(right)] = parent_value_sum

            for node in nodes_in_level:
                if id(node) in child_to_parent_value_sum:
                    node.val = total - child_to_parent_value_sum[id(node)]
                else:
                    node.val = 0

            if queue:
                queue.pop(0)
            
            queue.append(None)
        
        return root
