"""
    Question 2594: https://leetcode.com/problems/minimum-time-to-repair-cars/

    Classical question, just binary-search for the answer
"""

import math

class Solution:
    def isPossible(self, time: int, ranks: List[int], cars: int) -> bool:
        total_repaired_cars = 0
        for rank in ranks:
            repaired_cars = math.floor(math.sqrt(time / rank))
            total_repaired_cars = total_repaired_cars + repaired_cars
        return total_repaired_cars >= cars
    
    def binarySearch(self, start: int, end: int, ranks: List[int], cars: int):
        half = (start + end) // 2

        if self.isPossible(half, ranks, cars) and (half == start or not self.isPossible(half - 1, ranks, cars)):
            return half

        if self.isPossible(half, ranks, cars):
            return self.binarySearch(start, half - 1, ranks, cars)

        return self.binarySearch(half + 1, end, ranks, cars)

    def repairCars(self, ranks: List[int], cars: int) -> int:
        minimum = 1
        maximum = max(ranks) * cars**2

        return self.binarySearch(minimum, maximum, ranks, cars)
