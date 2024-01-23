"""
Question 1525: https://leetcode.com/problems/number-of-good-ways-to-split-a-string

I'd say this is actually an easy question
"""

class Solution:
    def numSplits(self, s: str) -> int:
        frequency_dict_left = {}
        frequency_dict_right = {}

        for i in range(0, len(s)):
            frequency_dict_right[s[i]] = frequency_dict_right.get(s[i], 0) + 1

        result = 0
        for i in range(0, len(s) - 1):
            frequency_dict_left[s[i]] = frequency_dict_left.get(s[i], 0) + 1
            frequency_dict_right[s[i]] = frequency_dict_right.get(s[i], 0) - 1
            if frequency_dict_right[s[i]] == 0:
                del frequency_dict_right[s[i]] 

            if len(frequency_dict_left) == len(frequency_dict_right):
                result = result + 1
        
        return result
