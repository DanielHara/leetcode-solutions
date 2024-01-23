"""
Question 1578: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
"""

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # Do it greedily:

        i = 0
        result = 0
        while i < len(colors):
            j = i
            while j < len(colors) and colors[j] == colors[i]:
                j = j + 1

            result = result + sum(neededTime[i:j]) - max(neededTime[i:j])

            i = j

        return result
