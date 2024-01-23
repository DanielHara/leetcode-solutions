# Question 2177: https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

"""
    Quite easy question, should be rated as Easy instead of Medium
"""

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        middle = num // 3

        result = [middle - 1, middle, middle + 1]

        if sum(result) == num:
            return result

        return []
