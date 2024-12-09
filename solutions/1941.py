# Question 1941: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

"""
  Trivial question
"""

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        frequency_dict = {}

        for char in s:
            frequency_dict[char] = frequency_dict.get(char, 0) + 1
        
        return len(set(frequency_dict.values())) == 1
