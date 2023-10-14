# Question 1394: https://leetcode.com/problems/find-lucky-integer-in-an-array/

"""
    Trivial question
"""

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        frequency_dict = {}

        for number in arr:
            frequency_dict[number] = frequency_dict.get(number, 0) + 1
        
        maximum = -1

        for [number, frequency] in frequency_dict.items():
            if number == frequency:
                maximum = max(number, maximum)
        
        return maximum
