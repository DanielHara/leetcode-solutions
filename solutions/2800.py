# Question 2800: https://leetcode.com/problems/shortest-string-that-contains-three-strings/

"""
    Just try all the possibilities
"""

class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        permutations = [[a, b, c], [a, c, b], [b, a, c], [b, c, a], [c, a, b], [c, b, a]]

        result = None
        for permutation in permutations:
            [first, second, third] = permutation

            possibility = second
            if third not in second:
                for k in range(min(len(second), len(third)), -1, -1):
                    if second[len(second) - k : len(second)] == third[0: k]:
                        possibility = possibility + third[k:]
                        break
            
            if first not in second:
                for k in range(min(len(first), len(second)), -1, -1):
                    if second[0:k] == first[len(first) - k : len(first)]:
                        possibility = first[0: len(first) - k] + possibility
                        break
            
            if result is None:
                result = possibility
            elif len(possibility) < len(result):
                result = possibility
            elif len(possibility) == len(result) and possibility < result:
                result = possibility
        
        return result
