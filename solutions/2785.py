# Question 2785: https://leetcode.com/problems/sort-vowels-in-a-string/

"""
    Just some manipulations, nothing fancy
"""

from functools import cmp_to_key

class Solution:    
    def sortVowels(self, s: str) -> str:
        lower_vowels = ['a', 'e', 'i', 'o', 'u']
        upper_vowels = [vowel.upper() for vowel in lower_vowels]
        vowels = lower_vowels + upper_vowels

        frequency_dict = {}
        for char in s:
            if char in vowels:
                frequency_dict[char] = frequency_dict.get(char, 0) + 1
        
        vowels_frequency = [list(element) for element in list(frequency_dict.items())]
        vowels_frequency.sort(key=lambda el: el[0])

        chars = [char for char in s]

        vowels_index = 0
        for index in range(len(chars)):
            if chars[index] in vowels:
                chars[index] = vowels_frequency[vowels_index][0]
                vowels_frequency[vowels_index][1] = vowels_frequency[vowels_index][1] - 1
                if vowels_frequency[vowels_index][1] == 0:
                    vowels_index = vowels_index + 1

        return ''.join(chars)

