# Question 2748: https://leetcode.com/problems/number-of-beautiful-pairs/

"""
    Trivial, but interesting question! I was wondering how to efficiently implement areCoprime if the operands
    are not just digits (1 to 9), but large integer numbers. That could be a nice follow-up question!
"""

class Solution:
    def areCoprime(self, a: int, b: int):
        for factor in range(2, min(a, b) + 1):
            if a % factor == 0 and b % factor == 0:
                return False
            
        return True

    def getFirstDigit(self, num: int) -> int:
        while num >= 10:
            num = num // 10

        return num
    
    def getLastDigit(self, num: int) -> int:
        return num % 10
    
    def countBeautifulPairs(self, nums: List[int]) -> int:
        N = len(nums)
        
        result = 0
        for i in range(N - 1):
            for j in range(i + 1, N):
                if self.areCoprime(self.getFirstDigit(nums[i]), self.getLastDigit(nums[j])):
                    result = result + 1

        return result
