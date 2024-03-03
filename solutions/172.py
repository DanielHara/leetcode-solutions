"""
    Question 172: https://leetcode.com/problems/factorial-trailing-zeroes/

    Very interesting question! I just wrote down a table and came up with the solution.
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0

        limit = 1
        while 5 ** limit <= n:
            result = result + n // (5 ** limit)
            limit = limit + 1

        return result
