"""
    Question 2405: https://leetcode.com/problems/optimal-partition-of-string/

    This question has no secret, just do it greedily.
"""

class Solution:
    def partitionString(self, s: str) -> int:
        i = 0

        result = 0
        while i < len(s):
            distinct_set = set()
            j = i

            while j < len(s) and s[j] not in distinct_set:
                distinct_set.add(s[j])
                j = j + 1

            i = j

            result = result + 1

        return result
