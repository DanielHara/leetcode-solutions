# Question 1647: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

"""
    Just create a dict with the frequencies of each characters and try brute force, which is ok, because there is
    a limited number of letters in the alphabet.
"""

class Solution:
    def minDeletions(self, s: str) -> int:
        frequency_dict = {}
        
        for char in s:
            frequency_dict[char] = frequency_dict.get(char, 0) + 1
        
        frequency_set = set()
        
        result = 0
        for value in frequency_dict.values():
            while value in frequency_set and value > 0:
                value = value - 1
                result = result + 1
            
            if value > 0:
                frequency_set.add(value)
        
        return result
