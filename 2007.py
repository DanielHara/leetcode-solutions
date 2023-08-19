# Question 2007: https://leetcode.com/problems/find-original-array-from-doubled-array/

"""
    Do it greedily: sort the array and start searching for the doubled values.
"""

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()

        frequency_dict = {}
        for number in changed:
            frequency_dict[number] = frequency_dict.get(number, 0) + 1
        
        result = []
        for element in changed:
            if frequency_dict[element] == 0:
                continue
            
            frequency_dict[element] = frequency_dict[element] - 1
            double = 2 * element
            if frequency_dict.get(double, 0) <= 0:
                return []
            
            frequency_dict[double] = frequency_dict[double] - 1
            result.append(element)
        
        return result
