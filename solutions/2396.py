"""
Question 2396: https://leetcode.com/problems/strictly-palindromic-number/

    A kinda unfortunate question. Consider writing the number in base (n - 2). It would need to be 1*(n - 2) + 2*1, which will
    never be a palindrome. Therefore, there's no strictly palindromic number. 
"""

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False
