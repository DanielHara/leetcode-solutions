# Question 1184: https://leetcode.com/problems/distance-between-bus-stops/description/

# Just do it, easy question!

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        N = len(distance)

        i = start
        a = 0
        while i != destination:
            a = a + distance[i]
            i = (i + 1) % N
        
        i = start
        b = 0
        while i != destination:
            i = (i - 1) % N
            b = b + distance[i]
        
        return min(a, b)
