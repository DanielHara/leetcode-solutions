# Question 3090: https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

"""
    A brute-force, O(N**2) solution would pass the judge, because 2 <= s.length <= 100
    A sliding window approach like the following is more efficient, solving the problem in O(N) time
"""

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        start = 0
        end = 0

        frequency_dict = {}
        result = 0
        while start < len(s):
            while end < len(s) and frequency_dict.get(s[end], 0) < 2:
                frequency_dict[s[end]] = frequency_dict.get(s[end], 0) + 1
                end = end + 1

            result = max(result, end - start)

            if frequency_dict[s[start]] > 1:
                frequency_dict[s[start]] = frequency_dict[s[start]] - 1
            else:
                del frequency_dict[s[start]]

            start = start + 1

        return result
