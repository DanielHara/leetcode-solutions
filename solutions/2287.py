# Question 2287: https://leetcode.com/problems/rearrange-characters-to-make-target-string/

"""
    Quite trivial question    
"""

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        frequency_dict_target = {}

        for char in target:
            frequency_dict_target[char] = frequency_dict_target.get(char, 0) + 1
        
        frequency_dict_s = {}
        for char in s:
            frequency_dict_s[char] = frequency_dict_s.get(char, 0) + 1
        
        result = len(s)

        for char in target:
            result = min(result, frequency_dict_s.get(char, 0) // frequency_dict_target[char])
        
        return result
