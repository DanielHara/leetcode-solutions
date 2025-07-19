# Question 788: https://leetcode.com/problems/rotated-digits/

"""
    I really don't know why this question is Medium, just do it, nothing fancy. 
"""

class Solution:
    def getRotatedDigit(self, digit: str) -> str:
        if digit == '0' or digit == '1' or digit == '8':
            return digit
        
        if digit == '2':
            return '5'
        
        if digit == '5':
            return '2'
        
        if digit == '6':
            return '9'
        
        if digit == '9':
            return '6'
        
        return None

    def getRotatedDigits(self, digits: str) -> str:
        rotated_digits = []
        for digit in digits:
            rotated_digit = self.getRotatedDigit(digit)
            if rotated_digit is None:
                return None

            rotated_digits.append(rotated_digit)
        
        return ''.join(rotated_digits)

    def rotatedDigits(self, n: int) -> int:
        result = 0

        for number in range(1, n + 1):
            rotated_digits = self.getRotatedDigits(str(number))

            if rotated_digits is not None and int(rotated_digits) != number:
                result = result + 1
        
        return result
