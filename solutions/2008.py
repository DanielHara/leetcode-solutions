# Question 2008: https://leetcode.com/problems/maximum-earnings-from-taxi/

"""
    Quite easy question, just use dynamic programming
"""

class Solution:
    # Returns the index of the leftmost ride for which ride[0] >= target. Returns None if there's none
    def binarySearch(self, rides: List[List[int]], i: int, j: int, target: int):
        if i > j:
            return None
        
        half = (i + j) // 2

        if rides[half][0] >= target and (half == i or rides[half - 1][0] < target):
            return half
    
        if rides[half][0] >= target:
            return self.binarySearch(rides, i, half - 1, target)

        return self.binarySearch(rides, half + 1, j, target)


    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda ride: ride[0])

        for ride in rides:
            ride.append(None)
        
        rides[-1][3] = rides[-1][2] + rides[-1][1] - rides[-1][0]
        
        for i in range(len(rides) - 2, -1, -1):
            ride = rides[i]

            end = ride[1]
            money = ride[1] - ride[0] + ride[2]

            index = self.binarySearch(rides, i + 1, len(rides) - 1, end)
            if index is not None:
                rides[i][3] = max(rides[i + 1][3], money + rides[index][3], money)
            else:
                rides[i][3] = max(rides[i + 1][3], money)
        
        return rides[0][3]

