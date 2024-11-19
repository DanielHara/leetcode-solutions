"""
    Question 1550: https://leetcode.com/problems/three-consecutive-odds/

    What is this question doing on Leetcode?
"""

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for index in range(len(arr) - 2):
            if arr[index] % 2 == 1 and arr[index + 1] % 2 == 1 and arr[index + 2] % 2 == 1:
                return True

        return False
