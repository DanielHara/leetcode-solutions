# Question 1317: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

"""
    Trivial solution, just brute-force
"""

class Solution:
    def isNoZeroInteger(self, n: int):
        while n > 0:
            if n % 10 == 0:
                return False

            n = n // 10
        
        return True


    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 1
        while True:
            b = n - a
            if self.isNoZeroInteger(a) and self.isNoZeroInteger(b):
                return [a,b]
            
            a = a + 1
