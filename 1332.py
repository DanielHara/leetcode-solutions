"""
Question 1332: https://leetcode.com/problems/remove-palindromic-subsequences/

If the string is a palindrome, return 1. Otherwise, just split the string into groups of "a"s and "b"s, each of which
is a palindrome (all the same letters)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        N = len(s)
        for i in range(int(N / 2)):
            if s[i] != s[N - 1 - i]:
                return False
        
        return True

    def removePalindromeSub(self, s: str) -> int:
        isPalindrome = self.isPalindrome(s)

        return 1 if isPalindrome else 2

