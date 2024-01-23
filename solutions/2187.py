# Question 2187: https://leetcode.com/problems/minimum-time-to-complete-trips/

class Solution:
    def isPossible(self, usedTime: int, time: List[int], totalTrips: int):
        trips = 0
        for element in time:
            trips = trips + usedTime // element
        
        result = trips >= totalTrips
        return result

    def binarySearch(self, lower_bound: int, upper_bound: int, time: List[int], totalTrips: int):
        if lower_bound > upper_bound:
            return None
        
        half = (lower_bound + upper_bound) // 2

        if self.isPossible(half, time, totalTrips) and (half == lower_bound or not self.isPossible(half - 1, time, totalTrips)):
            return half
        
        if self.isPossible(half, time, totalTrips):
            return self.binarySearch(lower_bound, half - 1, time, totalTrips)
        
        return self.binarySearch(half + 1, upper_bound, time, totalTrips)

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        maximum = totalTrips * max(time)
        
        return self.binarySearch(1, maximum, time, totalTrips)
