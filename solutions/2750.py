# Question 2750: https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

"""
    This question is very interesting! Just go through the array and find out which are the indexes which contain ones,
    and then the answer will come naturally.
"""

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        ones_indexes = []
        for index, num in enumerate(nums):
            if num == 1:
                ones_indexes.append(index)
        
        if len(ones_indexes) == 0:
            return 0
        
        mod = 10**9 + 7
        
        result = 1
        for index in range(len(ones_indexes) - 1, 0, -1):
            difference = ones_indexes[index] - ones_indexes[index - 1]
            result = (difference % mod) * (result % mod) % mod
        
        return result
