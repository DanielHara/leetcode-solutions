# Question 933: https://leetcode.com/problems/number-of-recent-calls/

"""
    Trivial question, and using collections.deque helps!
"""

from collections import deque

class RecentCounter:
    def __init__(self):
        self.deque = deque()

    def ping(self, t: int) -> int:
        self.deque.append(t)

        while self.deque[0] < t - 3000:
            self.deque.popleft()
        
        return len(self.deque)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)