# Question 1780: https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

"""
    I just was looking at the expression 3**k1 + 3**k2 + 3**kn, where k1 < k2 < ... < kn, and came up with
    the skeleton of the answer
"""

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n % 3 != 0:
            n = n - 1
        
        while n > 0:
            if n % 3 != 0:
                return False
            
            while n % 3 == 0:
                n = n // 3

            n = n - 1
            
        return True
