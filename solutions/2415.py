"""
    Question 2415: https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

    Not difficult, but still interesting question.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root, None]
        level = 0

        array = []

        while len(queue) >= 2:
            element = queue.pop(0)

            if element is None:
                if level % 2 == 1:
                    for i in range(0, len(array) // 2, 1):
                        temp = array[i].val
                        array[i].val = array[len(array) - 1 - i].val
                        array[len(array) - 1 - i].val = temp
                    
                    array = []

                level = level + 1
                continue
            
            if level % 2 == 1:
                array.append(element)
            
            if element.left:
                queue.append(element.left)
            
            if element.right:
                queue.append(element.right)
            
            if queue[0] == None:
                queue.append(None)
        
        return root
