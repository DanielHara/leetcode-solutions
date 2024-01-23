# Question 2358: https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

"""
    The solution is somewhat counterintutive, because you don't even need to know the values in the array.
    Just do it greedily as in the hint. If the array is sorted, get the groups with 1, 2, ..., N members. Then
    simply find the largest N for which 1 + 2 + ... + N is less or equal to len(grades)
"""

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        N = len(grades)

        return math.floor((-1 + math.sqrt(1 + 8*N)) / 2)
