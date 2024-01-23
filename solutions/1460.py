# Question 1460: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

"""
    Just check if their frequency dict is the same:
"""

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        frequency_dict_1 = {}
        for el in target:
            frequency_dict_1[el] = frequency_dict_1.get(el, 0) + 1
        
        frequency_dict_2 = {}
        for el in arr:
            frequency_dict_2[el] = frequency_dict_2.get(el, 0) + 1
        
        for el in frequency_dict_1:
            if frequency_dict_1[el] != frequency_dict_2.get(el, 0):
                return False
        
        for el in frequency_dict_2:
            if frequency_dict_2[el] != frequency_dict_1.get(el, 0):
                return False
        
        return True
