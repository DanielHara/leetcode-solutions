"""
Question 2414: https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

    Another trivial question labelled as "Medium" :(
"""


class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        result = 0

        i = 0
        while i < len(s):
            j = i + 1

            while j < len(s) and ord(s[j - 1]) == ord(s[j]) - 1:
                j = j + 1
            
            result = max(result, j - i)
            
            i = j
        
        return result
