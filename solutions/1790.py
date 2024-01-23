# Question 1790: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

"""
    A trivial, but interesting, question!
"""

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        differences = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                differences.append([s1[i], s2[i]])
        
            if len(differences) > 2:
                return False
        
        if len(differences) == 0:
            return True
        
        if len(differences) == 1:
            return False

        return differences[0][0] == differences[1][1] and differences[1][0] == differences[0][1]
