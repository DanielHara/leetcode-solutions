"""
    Question 475: https://leetcode.com/problems/heaters/

    Really nice question, first sort houses and heaters.
    Then write a function sPossible(self, houses: List[int], heaters: List[int], radius: int):
    which just returns if it's possible to heat the houses with a given radius.
    Then, use this function to binary search on the answer.
"""

class Solution:
    def binarySearch(self, houses: List[int], heaters: List[int], start: int, end: int):
        if start > end:
            return None
        
        half = (start + end) // 2
        if self.isPossible(houses, heaters, half) and (half == start or not self.isPossible(houses, heaters, half - 1)):
            return half
        if self.isPossible(houses, heaters, half):
            return self.binarySearch(houses, heaters, start, half - 1)
        return self.binarySearch(houses, heaters, half + 1, end)

    def isPossible(self, houses: List[int], heaters: List[int], radius: int):
        house_index = 0
        heater_index = 0

        while house_index < len(houses):
            if houses[house_index] < heaters[heater_index] - radius:
                return False
            elif houses[house_index] >= heaters[heater_index] - radius and houses[house_index] <= heaters[heater_index] + radius:
                house_index = house_index + 1
            else:
                if heater_index < len(heaters) - 1:
                    heater_index = heater_index + 1
                else:
                    return False
        
        return True
    
    # Just use binary search
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        return self.binarySearch(houses, heaters, 0, 10**9)
