# Question 728: https://leetcode.com/problems/self-dividing-numbers/

"""
    Trivial question
"""

class Solution:
    def isSelfDividing(self, num: int) -> bool:
        temp = num
        while temp > 0:
            digit = temp % 10
            if digit == 0:
                return False

            temp = temp // 10

            if num % digit != 0:
                return False
        
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        for index in range(left, right + 1):
            if self.isSelfDividing(index):
                result.append(index)
        
        return result
