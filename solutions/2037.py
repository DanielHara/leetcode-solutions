# Question 2037: hhttps://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

"""
    Quite trivial question, just do it greedily.
"""

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        result = 0
        for i in range(0, len(seats)):
            result = result + abs(seats[i] - students[i])

        return result
