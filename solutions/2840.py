# Question 2840: https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

"""
    Easy question, just take the frequency dicts of the subsequence of the string with even indexes, and the the subsequence of the string
    with odd indexes, and compare them.
"""

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        frequency_dict_even_s1_indexes = {}
        frequency_dict_odd_s1_indexes = {}

        for index, char in enumerate(s1):
            if index % 2 == 0:
                frequency_dict_even_s1_indexes[char] = frequency_dict_even_s1_indexes.get(char, 0) + 1
            else:
                frequency_dict_odd_s1_indexes[char] = frequency_dict_odd_s1_indexes.get(char, 0) + 1

        frequency_dict_even_s2_indexes = {}
        frequency_dict_odd_s2_indexes = {}
        for index, char in enumerate(s2):
            if index % 2 == 0:
                frequency_dict_even_s2_indexes[char] = frequency_dict_even_s2_indexes.get(char, 0) + 1
            else:
                frequency_dict_odd_s2_indexes[char] = frequency_dict_odd_s2_indexes.get(char, 0) + 1
        
        return frequency_dict_even_s1_indexes == frequency_dict_even_s2_indexes and frequency_dict_odd_s1_indexes == frequency_dict_odd_s2_indexes
