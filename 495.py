"""
Question 493: https://leetcode.com/problems/teemo-attacking/
"""

# Trivial question

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        
        for i in range(len(timeSeries)):
            if i > 0 and timeSeries[i] - timeSeries[i - 1] < duration:
                result = result + timeSeries[i] - timeSeries[i - 1]
            else:
                result = result + duration
        
        return result
