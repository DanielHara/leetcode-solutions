"""
    Question 2583: https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

    Not a difficult question. Just do it. I noticed many questions on Leetcode ask you to enumerate the levels
    of a binary tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = [root, None]

        sums = []
        s = 0
        while len(queue) >= 2:
            element = queue.pop(0)

            if element is None:
                sums.append(s)
                s = 0
                queue.append(None)
            else:
                s = s + element.val
                if element.left is not None:
                    queue.append(element.left)
                
                if element.right is not None:
                    queue.append(element.right)
        
        if s > 0:
            sums.append(s)
        
        sums.sort(reverse=True)
        
        return sums[k - 1] if k - 1 < len(sums) else -1

