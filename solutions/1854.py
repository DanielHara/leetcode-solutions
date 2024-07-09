# Question 1854: https://leetcode.com/problems/maximum-population-year/

"""
    Very interesting easy question, which is actually not that easy!
"""

from functools import cmp_to_key

class Solution:
    def sortEvent(self, event1, event2):
        if event1['time'] != event2['time']:
            return event1['time'] - event2['time']
        
        if event1['type'] == 'birth' and event2['type'] == 'death':
            return 1
        
        if event1['type'] == 'death' and event2['type'] == 'birth':
            return -1
        
        return 0

    def maximumPopulation(self, logs: List[List[int]]) -> int:
        events = []
        for [start, end] in logs:
            events.append({
                'time': start,
                'type': 'birth'
            })
            events.append({
                'time': end,
                'type': 'death'
            })
        
        best_year = None
        maximum_population = 0

        events.sort(key=cmp_to_key(self.sortEvent))

        balance = 0
        for event in events:
            if event['type'] == 'birth':
                balance = balance + 1
                if balance > maximum_population:
                    maximum_population = balance
                    best_year = event['time']
            else:
                balance = balance - 1
        
        return best_year
