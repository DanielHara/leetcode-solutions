# Question 2462: https://leetcode.com/problems/total-cost-to-hire-k-workers/

"""
    Use the same trick as in question 2353
"""

from functools import cmp_to_key
import heapq

class Solution:
    def comparisonFunction(self, candidate_entry1, candidate_entry2):
        (cost1, index1) = candidate_entry1
        (cost2, index2) = candidate_entry2

        if cost1 < cost2:
            return -1
        if cost1 > cost2:
            return 1
        
        if index1 < index2:
            return -1
        if index1 > index2:
            return 1

        return 0

    # Also use a heap, in the same way
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        key_function = cmp_to_key(self.comparisonFunction)
        heap = []

        i = 0
        while i < candidates:
            heapq.heappush(heap, (key_function((costs[i], i)), (costs[i], i)))
            i = i + 1
        
        j = len(costs) - 1
        while j >= 0 and j >= i and j >= len(costs) - candidates:
            heapq.heappush(heap, (key_function((costs[j], j)), (costs[j], j)))
            j = j - 1
        
        result = 0
        for _dummy in range(k):
            element = heapq.heappop(heap)
            (cost, index) = element[1]
            result = result + cost

            if i <= j:
                if index < i and i < len(costs):
                    heapq.heappush(heap, (key_function((costs[i], i)), (costs[i], i)))
                    i = i + 1
                elif index > j and j >= 0:
                    heapq.heappush(heap, (key_function((costs[j], j)), (costs[j], j)))
                    j = j - 1

        return result
