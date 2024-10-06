"""
    Question 2580: https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

    Very interesting question!
    First, use a stack to group the ranges which overlap. Remember the question "Merge intervals"?
    Then, it's easy to see that the number of ways to group the ranges is 2 ** overlapping_range_number, because the
    number of ways to pick any number of elements (from 0 to N) from a set with N elements is 2 ** N (remember your Combinatorial Analysis class??)
"""

class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        overlapping_ranges = []

        ranges.sort(key=lambda el: el[0])

        for rang in ranges:
            if not overlapping_ranges or overlapping_ranges[-1][1] < rang[0]:
                overlapping_ranges.append(rang)
            else:
                top_range = overlapping_ranges.pop()

                overlapping_ranges.append([min(top_range[0], rang[0]), max(top_range[1], rang[1])])
        
        overlapping_range_number = len(overlapping_ranges)

        return 2 ** overlapping_range_number % (10**9 + 7)
