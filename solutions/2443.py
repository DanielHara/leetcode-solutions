"""
    Question 2443: https://leetcode.com/problems/sum-of-number-and-its-reverse/

    I looked at the constraints: 0 <= num <= 10**5, and brute-forcing seemed reasonable to me.
"""

class Solution:
    def getReverseNumber(self, num: int) -> int:
        digits = []
        while num > 0:
            digits.append(num % 10)
            num = num // 10
        
        result = 0
        for i in range(len(digits) - 1, -1, -1):
            result = result + digits[i] * 10 ** (len(digits) - 1 - i)
        
        return result
    
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for candidate in range(0, num + 1, 1):
            if self.getReverseNumber(candidate) + candidate == num:
                return True

        return False
