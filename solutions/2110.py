# Question 2110: https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

"""
    Very similar to question 2348
"""

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        result = 0

        i = 0
        while i < len(prices):
            j = i + 1

            while j < len(prices) and prices[j - 1] == prices[j] + 1:
                j = j + 1
            
            N = j - i
            
            result = result + N * (N + 1) // 2

            i = j

        return result
