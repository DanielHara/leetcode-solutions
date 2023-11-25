# Question 2236: https://leetcode.com/problems/root-equals-sum-of-children/

"""
    Very trivial, even stupid question. I don't know why it's on Leetcode :/
"""

class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.right.val + root.left.val
