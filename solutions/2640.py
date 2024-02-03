# Question 2640: https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

"""
    Just use some tricks with prefix sum / max. Not difficult
"""

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        prefix_max = []

        for num in nums:
            prefix_max.append(num if not prefix_max else max(num, prefix_max[-1]))

        conver = []
        for index, num in enumerate(nums):
            conver.append(num + prefix_max[index])

        prefix_sum_conv = []

        for num in conver:
            prefix_sum_conv.append(num if not prefix_sum_conv else (num + prefix_sum_conv[-1]))

        return prefix_sum_conv
