# Question 9: https://leetcode.com/problems/palindrome-number/

"""
    Not a particulary difficult question. I've written this solution without using more memory to store the
    number as a string (as suggested in the follow-up), simply by extracting the most significant digit and least significant digit in each
    interaction, and comparing them.
"""

class Solution:
    def getOrderOfMagnitude(self, x: int) -> int:
        n = 0
        
        while 10 ** (n + 1) <= x:
            n = n + 1
        
        return n
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        i = self.getOrderOfMagnitude(x)
        
        while i >= 1:
            a = x % 10
            b = int(x / (10 ** i))
            
            if a != b:
                return False
            
            x = int((x - a - b * 10 ** i) / 10)
            
            i = i - 2
        
        return True
