# Question 2070: https://leetcode.com/problems/most-beautiful-item-for-each-query/

"""
  Very similar to question 2054
"""

class Solution:
    # returns the right-most element for which element[0] <= target, returns None if there's none
    def binarySearch(self, S: List[int], i: int, j: int, target: int):
        if i > j:
            return None

        half = (i + j) // 2
        if S[half][0] <= target and (half == j or S[half + 1][0] > target):
            return S[half]
        
        if S[half][0] <= target:
            return self.binarySearch(S, half + 1, j, target)
        
        return self.binarySearch(S, i, half - 1, target)


    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda item: item[0])

        S = [None for i in range(len(items))]
        S[0] = [items[0][0], items[0][1]]

        for i in range(1, len(items), 1):
            item = items[i]
            S[i] = [item[0], max(S[i - 1][1], item[1])]

        result = []
        for query in queries:
            possibility = self.binarySearch(S, 0, len(S) - 1, query)

            result.append(possibility[1] if possibility else 0)
        
        return result
