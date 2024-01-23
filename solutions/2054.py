# Question 2054: https://leetcode.com/problems/two-best-non-overlapping-events/

"""
    Just use a bit of DP + Binary Search to do the trick
"""

class Solution:
    # returns the left-most element for which element[0] > target, returns None if there's none
    def binarySearch(self, S: List[int], i: int, j: int, target: int):
        if i > j:
            return None

        half = (i + j) // 2
        if S[half][0] > target and (half == i or S[half - 1][0] <= target):
            return S[half]

        if S[half][0] > target:
            return self.binarySearch(S, i, half - 1, target)
        
        return self.binarySearch(S, half + 1, j, target)


    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Just use some dynamic programming
        events.sort(key=lambda event: event[0])

        S = [None for i in range(len(events))]
        S[-1] = [events[-1][0], events[-1][2]]
        for i in range(len(events) - 2, -1, -1):
            event = events[i]
            S[i] = [event[0], max(S[i + 1][1], event[2])]

        result = events[-1][2]
        for i in range(0, len(events) - 1, 1):
            event = events[i]

            best = self.binarySearch(S, 0, len(S) - 1, event[1])
            if best is not None:
                possibility = event[2] + best[1]

                result = max(result, possibility)
        
            result = max(result, event[2])

        return result
