# Question 1881: https://leetcode.com/problems/maximum-value-after-insertion/

"""
    Quite easy question, just do it greedily.
"""


class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] != '-':
            i = 0
            while i < len(n) and int(n[i]) >= x:
                i = i + 1
            
            return n[:i] + str(x) + n[i:]
        
        i = 1
        while i < len(n) and int(n[i]) <= x:
            i = i + 1
            
        return n[:i] + str(x) + n[i:]
