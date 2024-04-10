# Question 1822: https://leetcode.com/problems/sign-of-the-product-of-an-array/

"""
    Trivial question
"""

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1

        for num in nums:
            if num == 0:
                return 0
            
            if num < 0:
                result = result * (-1)
        
        return result
