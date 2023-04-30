"""
Question 1189: https://leetcode.com/problems/maximum-number-of-balloons/

Trivial question
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        frequency_dict = {}

        for char in text:
            frequency_dict[char] = frequency_dict.get(char, 0) + 1
        
        frequency_dict_balloon = {}
        for char in 'balloon':
            frequency_dict_balloon[char] = frequency_dict_balloon.get(char, 0) + 1
        
        result = None
        for char in frequency_dict_balloon:
            if result is None:
                result = frequency_dict.get(char, 0) // frequency_dict_balloon[char]
            else:
                result = min(result, frequency_dict.get(char, 0) // frequency_dict_balloon[char])
        
        return result
