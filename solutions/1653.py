# Question 1653: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

"""
    Dynamic programming did help me out here.
"""

class Solution:
    def minimumDeletions(self, s: str) -> int:
        groups = []
        
        i = 0
        
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j = j + 1
            
            groups.append((s[i], j - i))
            
            i = j
        

        S = [None for i in range(len(groups))]
        S[-1] = 0
        
        a_occurences = groups[-1][1] if groups[-1][0] == 'a' else 0
        
        for i in range(len(groups) - 2, -1, -1):
            if groups[i][0] == 'a':
                S[i] = S[i + 1]
                a_occurences = a_occurences + groups[i][1]
            else:
                S[i] = min(a_occurences, groups[i][1] + (S[i + 2] if i + 2 < len(S) else 0))
        
        if groups[0][0] == 'b':
            return S[0]
        
        return S[1] if len(S) > 1 else 0
