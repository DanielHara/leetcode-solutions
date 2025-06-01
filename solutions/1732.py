# Question 1732: https://leetcode.com/problems/find-the-highest-altitude

"""
    Just an easy warm-up question
"""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0

        result = 0
        for element in gain:
            current_altitude = current_altitude + element
            result = max(result, current_altitude)
        
        return result
