# Question 844: https://leetcode.com/problems/backspace-string-compare/

"""
   Compare the characters in the string from right to left, and count the backspaces.
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        
        a = 0
        b = 0
        while i >= 0 or j >= 0:
            while a > 0 and i >= 0:
                if s[i] == '#':
                    a = a + 1
                else:
                    a = a - 1
                i = i - 1
            
            while b > 0 and j >= 0:
                if t[j] == '#':
                    b = b + 1
                else:
                    b = b - 1
                j = j - 1
                
            if i >= 0 and s[i] == '#':
                a = a + 1
                i = i - 1
            elif j >= 0 and t[j] == '#':
                b = b + 1
                j = j - 1
            else:
                if (i >= 0 and j < 0) or (i < 0 and j >= 0):
                    return False
                
                if i >= 0 and j >= 0 and s[i] != t[j]:
                    return False
                
                i = i - 1
                j = j - 1
            
        return i < 0 and j < 0
