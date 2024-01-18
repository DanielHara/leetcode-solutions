"""
    Question 2476: https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

    Just flatten the tree and use binary search, no secrets here

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flattenTree(self, root: Optional[TreeNode], result_array):
        if not root:
            return result_array

        self.flattenTree(root.left, result_array)        
        result_array.append(root.val)
        self.flattenTree(root.right, result_array)

        return result_array

    # Gives you the largest value for which nums[index] >= target. Returns -1 if there's None
    def binarySearch2(self, i: int, j: int, nums: List[int], target: int):
        if i > j:
            return -1
        
        half = (i + j) // 2
        
        if nums[half] >= target and (half == i or nums[half - 1] < target):
            return nums[half]
        
        if nums[half] >= target:
            return self.binarySearch2(i, half - 1, nums, target)
        
        return self.binarySearch2(half + 1, j, nums, target)
    
    # Gives you the largest value for which nums[index] <= target. Returns -1 if there's None
    def binarySearch1(self, i: int, j: int, nums: List[int], target: int):
        if i > j:
            return -1
        
        half = (i + j) // 2

        if nums[half] <= target and (half == j or nums[half + 1] > target):
            return nums[half]
        
        if nums[half] <= target:
            return self.binarySearch1(half + 1, j, nums, target)
        
        return self.binarySearch1(i, half - 1, nums, target)


    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        flattened_tree = self.flattenTree(root, [])
        
        answer = []
        for query in queries:
            answer.append([self.binarySearch1(0, len(flattened_tree) - 1, flattened_tree, query), self.binarySearch2(0, len(flattened_tree) - 1, flattened_tree, query)])
        
        return answer
