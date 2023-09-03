"""
Question 2121: https://leetcode.com/problems/intervals-between-identical-elements/

Not a difficult question, just use a bit do DP.
"""

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        index_dict = {}

        for index, number in enumerate(arr):
            if number not in index_dict:
                index_dict[number] = []

            index_dict[number].append(index)

        result = [None for i in range(len(arr))]
        for v in index_dict.values():
            S = 0
            # Calculate the first one:

            for i in range(1, len(v), 1):
                S = S + v[i] - v[0]
            result[v[0]] = S

            for i in range(1, len(v), 1):
                S = S - (v[i] - v[i - 1]) * (len(v) - 1 - i) + (v[i] - v[i - 1])*(i - 1)
                result[v[i]] = S

        return result
