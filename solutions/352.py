# Question 352: https://leetcode.com/problems/data-stream-as-disjoint-intervals/

"""
    Quite straightforward "hard" question. Just take advantage of the fact that getIntervals will be called far less often than addNum, and
    therefore can be a lot more expensive than addNum. You can essentially brute-force getIntervals.
    This answer beats 100% of accepted submissions in processing time, and 69.13% in memory usage.
"""

class SummaryRanges:
    def __init__(self):
        self.number_set = set()
        self.intervals = []

    def addNum(self, value: int) -> None:
        if value in self.number_set:
            return
        
        self.number_set.add(value)
        self.intervals.append([value, value])

    def getIntervals(self) -> List[List[int]]:
        sorted_intervals = sorted(self.intervals, key=lambda interval: interval[0])

        stack = []
        for interval in sorted_intervals:
            if not stack:
                stack.append(interval)
            elif stack[-1][1] + 1 >= interval[0]:
                start = stack[-1][0]
                stack.pop()
                stack.append([start, interval[1]])
            else:
                stack.append(interval)

        self.intervals = stack

        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
