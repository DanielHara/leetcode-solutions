"""
    Question 2332: https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

    This question is very interesting! Goes further than question 2410: https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/
"""

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        passengers.sort()
        buses.sort()

        result = min(buses[0], passengers[0] - 1)

        bus_index = 0
        passenger_index = 0
        while bus_index < len(buses):
            weight = 0

            while passenger_index < len(passengers) and passengers[passenger_index] <= buses[bus_index] and weight < capacity:
                weight = weight + 1
                if passenger_index > 0 and passengers[passenger_index] != passengers[passenger_index - 1] + 1:
                    result = passengers[passenger_index] - 1
                elif passenger_index == 0:
                    result = passengers[passenger_index] - 1

                passenger_index = passenger_index + 1
            
            if weight < capacity:
                if not (passenger_index - 1 >= 0 and passengers[passenger_index - 1] == buses[bus_index]):
                    result = buses[bus_index]

            bus_index = bus_index + 1

        return result
