"""
    Question 2563: https://leetcode.com/problems/count-the-number-of-fair-pairs/
    
    Nothing fancy, just use some binary-search.
    By the way, this relates strongly to a question I want to solve: https://leetcode.com/problems/count-of-range-sum/description/
"""

class Solution:
    # Returns the smallest index for which nums[index] >= target. Returns None if there's none
    def binarySearch1(self, nums: List[int], i: int, j: int, target: int):
        if i > j:
            return None
        
        half = (i + j) // 2
        if nums[half] >= target and (half == i or nums[half - 1] < target):
            return half
        
        if nums[half] >= target:
            return self.binarySearch1(nums, i, half - 1, target)
        
        return self.binarySearch1(nums, half + 1, j, target)
    
    # Returns the largest index for which nums[index] <= target. Returns None if there's none
    def binarySearch2(self, nums: List[int], i: int, j: int, target: int):
        if i > j:
            return None
        
        half = (i + j) // 2
        if nums[half] <= target and (half == j or nums[half + 1] > target):
            return half
        
        if nums[half] <= target:
            return self.binarySearch2(nums, half + 1, j, target)
        
        return self.binarySearch2(nums, i, half - 1, target)
    
    
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        result = 0

        for index, num in enumerate(nums):
            lower_index = self.binarySearch1(nums, 0, len(nums) - 1, lower - num )
            upper_index = self.binarySearch2(nums, 0, len(nums) - 1, upper - num)

            if lower_index is None or upper_index is None:
                continue
            
            if lower_index <= index and index <= upper_index:
                result = result + upper_index - lower_index
            else:
                result = result + upper_index - lower_index + 1
        
        return result // 2
