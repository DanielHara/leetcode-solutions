# Question 1122: https://leetcode.com/problems/relative-sort-array/

"""
    Quite a trivial question
"""

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        frequency_dict = {}

        for number in arr1:
            frequency_dict[number] = frequency_dict.get(number, 0) + 1
        
        result = []
        for number in arr2:
            for repeat in range(frequency_dict[number]):
                result.append(number)
            del frequency_dict[number]
        
        remainings = list(frequency_dict.items())
        remainings.sort(key=lambda el: el[0])

        for [remaining_number, remaining_frequency] in remainings:
            for repeat in range(remaining_frequency):
                result.append(remaining_number)
        
        return result
