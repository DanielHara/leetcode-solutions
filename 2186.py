# Question 2186: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

"""
    Definitely not a difficult question
"""

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        frequency_dict_s = {}
        for char in s:
            frequency_dict_s[char] = frequency_dict_s.get(char, 0) + 1
        
        frequency_dict_t = {}
        for char in t:
            frequency_dict_t[char] = frequency_dict_t.get(char, 0) + 1
        
        result = 0
        for index in range(ord('a'), ord('z') + 1, 1):
            result = result + abs(frequency_dict_s.get(chr(index), 0) - frequency_dict_t.get(chr(index), 0))

        return result
