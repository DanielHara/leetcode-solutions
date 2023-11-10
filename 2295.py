# Question 2295: https://leetcode.com/problems/replace-elements-in-an-array/

"""
    Just use a map from values to indexes to do the trick
"""

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        values_to_index_dict = {}

        for index, num in enumerate(nums):
            values_to_index_dict[num] = index

        for operation in operations:
            [number_to_replace, replacement] = operation

            index_to_replace = values_to_index_dict[number_to_replace]
            nums[index_to_replace] = replacement

            del values_to_index_dict[number_to_replace]
            values_to_index_dict[replacement] = index_to_replace

        return nums
