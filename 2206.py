# Question 2206: https://leetcode.com/problems/divide-array-into-equal-pairs/

"""
Basically, it's possible to divide the array into equal pairs if, and only if,
the frequency of all the elements is even
"""

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        frequency_dictionary = {}
        
        for num in nums:
            frequency_dictionary[num] = frequency_dictionary.get(num, 0) + 1
        
        for value in frequency_dictionary.values():
            if value % 2 != 0:
                return False

        return True        
