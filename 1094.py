# Question 1094: https://leetcode.com/problems/car-pooling/

"""
    A very interesting question! Instead of intervals, think in pick-up and drop-off events.
    Merging intervals probably will give you a O(N**2) solution, which is not good enough.
"""

import functools

class Solution:
    def compare(self, event1, event2):
        if event1['location'] != event2['location']:
            return event1['location'] - event2['location']

        if event1['type'] == 'origin' and event2['type'] == 'destination':
            return 1

        if event2['type'] == 'origin' and event1['type'] == 'destination':
            return -1

        return 0

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for [numPassengers, origin, destination] in trips:
            events.append({
                'type': 'origin',
                'location': origin,
                'numPassengers': numPassengers,
            })

            events.append({
                'type': 'destination',
                'location': destination,
                'numPassengers': numPassengers,
            })
        
        events.sort(key=functools.cmp_to_key(self.compare))

        numPassengers = 0
        for event in events:
            if event['type'] == 'origin':
                numPassengers = numPassengers + event['numPassengers']
                if numPassengers > capacity:
                    return False
            else:
                numPassengers = numPassengers - event['numPassengers']

        return True
