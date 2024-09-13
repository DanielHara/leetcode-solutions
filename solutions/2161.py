# Question 2161: https://leetcode.com/problems/partition-array-according-to-given-pivot/

"""
    You can tweak a sorting function to do it.
    Or just keep 2 lists: one with the elements less than the pivot, and another one with the elements greater than the pivot.
    Then, just go through them to get the result.
"""

from functools import cmp_to_key

class Solution:
    def sort(self, num1: int, num2: int):
        if num1 > self.pivot and num2 > self.pivot:
            return 0

        if num1 < self.pivot and num2 < self.pivot:
            return 0

        return num1 - num2

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        self.pivot = pivot

        nums.sort(key=cmp_to_key(self.sort))

        return nums
