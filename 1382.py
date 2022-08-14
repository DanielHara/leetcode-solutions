# Question 1382: https://leetcode.com/problems/balance-a-binary-search-tree/

"""
    Do it greedily, just flatten the tree into an increasing array (it's a binary search tree, after all),
    and always get the element in the middle, and recursively build your tree this way.
"""

class Solution:
    def get_array(self, root: TreeNode) -> TreeNode:
        if not root:
            return []
        
        return self.get_array(root.left) + [root.val] + self.get_array(root.right)
    
    def recursiveBalanceBST(self, i: int, j: int, array: List[int]) -> TreeNode:
        if i > j:
            return None
        
        half = (i + j) // 2
        
        root = TreeNode(array[half])
        
        root.left = self.recursiveBalanceBST(i, half - 1, array)
        root.right = self.recursiveBalanceBST(half + 1, j, array)
        
        return root
    
    def balanceBST(self, root: TreeNode) -> TreeNode:    
        array = self.get_array(root)
        
        return self.recursiveBalanceBST(0, len(array) - 1, array)
