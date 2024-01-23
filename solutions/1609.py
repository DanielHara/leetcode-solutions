# Question 1609: https://leetcode.com/problems/even-odd-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # Explore tree using a queue:
        queue = [root, None]
        
        level = 0
        
        ant_node = None
        while len(queue) > 1:
            node = queue.pop(0)
            
            if node is None:
                level = level + 1
                queue.append(None)
                ant_node = None
            else:
                if level % 2 == 0:
                    if node.val % 2 != 1:
                        return False
                    
                    if ant_node and node.val <= ant_node.val:
                        return False
                else:
                    if node.val % 2 == 1:
                        return False
                    
                    if ant_node and node.val >= ant_node.val:
                        return False

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                ant_node = node
        
        return True
