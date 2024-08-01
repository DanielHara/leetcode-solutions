# Question 1389: https://leetcode.com/problems/create-target-array-in-the-given-order/

"""
    Just do what you're told.
    The constraints
        1 <= nums.length, index.length <= 100
    hint at the fact that the solution will be trivial.
"""

class Solution:
    def createTargetArray(self, nums: List[int], indexes: List[int]) -> List[int]:
        target = []

        for i, index in enumerate(indexes):
            target.insert(index, nums[i])
        
        return target
