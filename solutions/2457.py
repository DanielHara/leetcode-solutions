"""
    Question 2457: https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

    This is a super cool question!
    Like, an example like n = 467, target = 6
    Your only change of decreasing the sum of the sum of the digits of n is increasing n in a way that you get
    digits of 0.
    Like, at first add 3 to n, to get 470. Then add 30 to get 500.
    Keep doing that until you have a number whose sum of its digits is less or equal to target.
"""

class Solution:
    def getDigits(self, value):
        digits = []
        while value > 0:
            digits.append(value % 10)
            value = value // 10

        digits.reverse()
        return digits    

    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        result = 0
        power = 0

        digits = self.getDigits(n)
        while sum(digits) > target:
            significant_digit = digits[len(digits) - 1 - power]
            amount_to_sum = (10 - significant_digit) * 10 ** power
            result = amount_to_sum + result
            n = n + amount_to_sum
            digits = self.getDigits(n)
            power = power + 1
        
        return result
