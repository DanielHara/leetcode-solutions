# Question 1870: https://leetcode.com/problems/minimum-speed-to-arrive-on-time/description/

"""
    Up from a certain speed, it's possible to arrive on time. So, just write a isPossible function
    and binary-search for the answer.
"""

class Solution:
    def isPossible(self, speed: int, dist: List[int], hour: int) -> bool:
        time = 0
        for i in range(0, len(dist) - 1):
            time = time + math.ceil(dist[i] / speed)
        
        time = time + dist[-1] / speed

        return time <= hour

    def binarySearch(self, lower_bound: int, upper_bound: int, dist: List[int], hour: int):
        if lower_bound > upper_bound:
            return None

        half = (lower_bound + upper_bound) // 2

        if self.isPossible(half, dist, hour) and (half == lower_bound or not self.isPossible(half - 1, dist, hour)):
            return half
        
        if self.isPossible(half, dist, hour):
            return self.binarySearch(lower_bound, half - 1, dist, hour)
        
        return self.binarySearch(half + 1, upper_bound, dist, hour)

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        answer = self.binarySearch(1, 10**7, dist, hour)
        
        return answer if answer is not None else -1
