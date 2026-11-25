# Question 738: https://leetcode.com/problems/monotone-increasing-digits/

"""
    Cool question! Do it greedily
"""


class Solution:
    def buildNumberFromDigits(self, digits):
        result = 0

        power = 0
        while digits:
            result = result + 10 ** power * digits.pop()
            power = power + 1
        
        return result
    
    def getDigits(self, n):
        reversed_digits = []
        while n > 0:
            reversed_digits.append(n % 10)
            n = n // 10

        digits = list(reversed(reversed_digits))

        return digits
    
    def isMonotonicallyIncreasing(self, digits):
        for i in range(0, len(digits) - 1, 1):
            if digits[i] > digits[i + 1]:
                return False

        return True
    
    def getCandidate(self, n):
        digits = self.getDigits(n)

        sufix_mins = [None for i in range(len(digits))]

        for i in range(len(digits) - 1, -1, -1):
            sufix_mins[i] = min(digits[i], sufix_mins[i + 1]) if i + 1 < len(digits) else digits[i]

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] > sufix_mins[i]:
                digits[i] = digits[i] - 1
                for j in range(i + 1, len(digits), 1):
                    digits[j] = 9

                return digits
        
        return digits


    def monotoneIncreasingDigits(self, n: int) -> int:
        candidate_digits = self.getDigits(n)

        while not self.isMonotonicallyIncreasing(candidate_digits):
            candidate_digits = self.getCandidate(self.buildNumberFromDigits(candidate_digits))
        
        return self.buildNumberFromDigits(candidate_digits)
