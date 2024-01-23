# Question 821: https://leetcode.com/problems/shortest-distance-to-a-character/

"""
    Just do it
"""

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indexes = []

        for index, char in enumerate(s):
            if char == c:
                indexes.append(index)

        result = [0 for i in range(len(s))]

        for i in range(0, indexes[0]):
            result[i] = indexes[0] - i
        
        for i in range(indexes[-1], len(s)):
            result[i] = i - indexes[-1]

        for i in range(len(indexes) - 1):
            for j in range(indexes[i], indexes[i + 1]):
                result[j] = min(j - indexes[i], indexes[i + 1] - j)
        
        return result
