# Question 1486: https://leetcode.com/problems/xor-operation-in-an-array/

"""
    Just do it, trivial question
"""

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0

        for i in range(0, n):
            result = result ^ (start + 2 * i)

        return result
