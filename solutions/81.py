# Question 81: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

"""
    Interesting, this trivial solution with sequential search is accepted at the 100 percentile in run time, LOL

    As there may be multiple repeated values, there's no solution better than O(N) in the worst case.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums
