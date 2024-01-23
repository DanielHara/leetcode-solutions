# Question 2150: https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

"""
    In any question for which the order of elements in an array doesn't matter (like this one),
    consider making a set or frequency dictionary out of it.
"""

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq_dict = {}
        
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        
        result = []
        for [key, freq] in freq_dict.items():
            if freq == 1 and ((key + 1) not in freq_dict and (key - 1) not in freq_dict):
                result.append(key)
        
        return result
