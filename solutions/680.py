# Question 680: https://leetcode.com/problems/valid-palindrome-ii/description/

"""
    Interesting question, and actually not that easy.
"""

class Solution:
    def isSubstringPalindrome(self, s: str, start: int, end: int) -> bool:
        if start > end:
            return True
        
        while start < end:
            if s[start] != s[end]:
                return False
            
            start = start + 1
            end = end - 1
        
        return True

    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                # In this case, you can delete s[start]
                if s[start + 1] == s[end]:
                    if self.isSubstringPalindrome(s, start + 1, end):
                        return True
                # In this case, you can delete s[end]
                if s[start] == s[end - 1]:
                    if self.isSubstringPalindrome(s, start, end - 1):
                        return True
                return False

            start = start + 1
            end = end - 1

        return True
