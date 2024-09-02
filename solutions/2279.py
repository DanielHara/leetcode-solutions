# Question 2279: https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

"""
    Very easy question, just do it greedily
"""

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diffs = []        
        for index in range(len(rocks)):
            diffs.append(capacity[index] - rocks[index])
        
        diffs.sort(reverse=True)

        result = 0
        while diffs and additionalRocks > 0:
            diff = diffs.pop()
            if additionalRocks < diff:
                return result
            additionalRocks = additionalRocks - diff
            result = result + 1
        
        return result
