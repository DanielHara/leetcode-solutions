"""
    Question 2406: https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups

    Quite interesting question. I used a trick similar to the one I used for question 1109.
"""

import functools

class Solution:
    def comparison_function(self, event1, event2):
        if event1[0] != event2[0]:
            return event1[0] - event2[0]
        
        if event1[1] == 'start':
            return -1
        
        if event1[1] == 'end':
            return 1
        
        return 0

    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []

        for [start, end] in intervals:
            events.append([start, 'start'])
            events.append([end, 'end'])
        
        events.sort(key=functools.cmp_to_key(self.comparison_function))

        balance = 0
        result = 0

        for [point, event_type] in events:
            if event_type == 'start':
                balance = balance + 1
            else:
                balance = balance - 1
            
            result = max(result, balance)
        
        return result
