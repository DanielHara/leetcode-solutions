# Question 1109: https://leetcode.com/problems/corporate-flight-bookings

"""
    Another very interesting question!
    I did the same as in question 1094, https://leetcode.com/problems/car-pooling/, and used prefix sum to do the trick.
    Just think as follows:
        "first" and "seats" is an event, where "seats" passengers board
        "last" and "seats" is an event, where "seats" passengers get off the flights
    Then just use prefix-sum to get the answer.
"""

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0 for i in range(n)]

        for [first, last, seats] in bookings:
            result[first - 1] = result[first - 1] + seats
            if last < n:
                result[last] = result[last] - seats
        
        for i in range(1, len(result), 1):
            result[i] = result[i - 1] + result[i]
        
        return result
