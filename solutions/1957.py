# Question 1957: https://leetcode.com/problems/delete-characters-to-make-fancy-string/

"""
  Very nice warm-up question!
"""

class Solution:
    def makeFancyString(self, s: str) -> str:
        start = 0
        end = start

        tokens = []
        result = 0

        while start < len(s):
            while end < len(s) and s[end] == s[start]:
                end = end + 1
            
            if end - start >= 3:
                tokens.append(s[start] * 2)
            else:
                tokens.append(s[start:end])
        
            start = end
        
        return ''.join(tokens)
