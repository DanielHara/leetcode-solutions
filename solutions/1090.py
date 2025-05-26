# Question 1090: https://leetcode.com/problems/largest-values-from-labels/

"""
    Just do it greedily, always take the highest value you can use and add them up.
"""

import heapq

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        values_heap = []

        result = 0
        for index in range(len(values)):
            value = values[index]
            label = labels[index]
            heapq.heappush(values_heap, (-value, (value, label)))

        result = 0
        used_items = 0

        used_labels_frequency = {}

        while values_heap:
            (dummy, value_label_pair) = heapq.heappop(values_heap)

            (value, label) = value_label_pair

            if used_labels_frequency.get(label, 0) < useLimit:
                used_labels_frequency[label] = used_labels_frequency.get(label, 0) + 1
                result = result + value
                used_items = used_items + 1

            if used_items == numWanted:
                return result

        return result
