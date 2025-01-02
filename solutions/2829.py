"""
    Question 2829: https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

    Easy question, just use a set instead of an array, and before adding a new item, check
    if you'd create a pair summing to k.
"""

class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        used_set = set()

        current = 1
        while len(used_set) < n:
            if k - current not in used_set:
                used_set.add(current)
            current = current + 1

        return sum(used_set)
