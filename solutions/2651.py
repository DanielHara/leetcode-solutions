# Question 2651: https://leetcode.com/problems/calculate-delayed-arrival-time/

"""
    What is this question even doing on Leetcode?
"""

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24
