# Question 1281: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

"""
    Trivial question
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digit_frequency = {}

        while n > 0:
            digit = n % 10
            digit_frequency[digit] = digit_frequency.get(digit, 0) + 1
            n = n // 10
        
        S = 0
        P = 1
        for [key, value] in digit_frequency.items():
            S = S + key * value
            P = P * key ** value
        
        return P - S
