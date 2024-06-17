"""
    Question 2486: https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

    Quite easy question, just do it greedily
"""

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_index = 0
        t_index = 0

        while s_index < len(s) and t_index < len(t):
            while s_index < len(s) and s[s_index] != t[t_index]:
                s_index = s_index + 1
            
            if s_index < len(s):
                s_index = s_index + 1
                t_index = t_index + 1
            else:
                return len(t) - t_index

        return len(t) - t_index
