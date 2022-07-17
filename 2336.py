# Question 2336: https://leetcode.com/problems/smallest-number-in-infinite-set/

"""
Just followed the hint:
        Based on the constraints, what is the maximum element that can possibly be popped?
So, basically, the maximum you can pop is 1000, so make a set with 1000 and perform the operations described.
You can use a heap to get always the smallest element that is in the set.
"""

class SmallestInfiniteSet:
    def __init__(self):
        self.heap = []
        self.set = {}

        for i in range(1, 1001):
            heapq.heappush(self.heap, i)
            self.set[i] = True
        

    def popSmallest(self) -> int:
        el = heapq.heappop(self.heap)
        self.set[el] = False

        return el

    def addBack(self, num: int) -> None:
        if self.set.get(num, False):
            return
        
        self.set[num] = True
        
        heapq.heappush(self.heap, num)
