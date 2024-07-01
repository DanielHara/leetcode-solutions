"""
    Question 2471: https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

    Interesting question, just do it
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def numberSwaps(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        position_dict = {}
        for index, num in enumerate(nums):
            position_dict[num] = index
        
        result = 0
        for index in range(len(nums)):
            if nums[index] != sorted_nums[index]:
                position = position_dict[sorted_nums[index]]

                temp = nums[index]
                nums[index] = nums[position]
                nums[position] = temp

                position_dict[temp] = position

                result = result + 1
        
        return result

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = [root, None]

        result = 0
        while len(queue) > 1:
            nodes_at_this_level = []
            while queue:
                node = queue.pop(0)

                if node is None:
                    break
                
                nodes_at_this_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result = result + self.numberSwaps(nodes_at_this_level)

            queue.append(None)
        
        return result
