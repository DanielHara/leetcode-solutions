# Question 1845: https://leetcode.com/problems/seat-reservation-manager/description/

"""
    If the question says "smallest-numbered", always suspect you have to use a heap.
"""

import heapq

class SeatManager:
    def __init__(self, n: int):
        self.reserved_seats = set()
        self.unreserved_seats_heap = []
        for seat in range(1, n + 1):
            heapq.heappush(self.unreserved_seats_heap, seat)

    def reserve(self) -> int:
        while self.unreserved_seats_heap:
            seat = heapq.heappop(self.unreserved_seats_heap)
            if seat not in self.reserved_seats:
                self.reserved_seats.add(seat)
                return seat

    def unreserve(self, seatNumber: int) -> None:
        self.reserved_seats.remove(seatNumber)
        heapq.heappush(self.unreserved_seats_heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)