"""
    Question 2610: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

    Also quite simple question, just do it greedily.
"""

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        frequency_dict = {}

        for num in nums:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1
        
        result = []
        for [num, frequency] in frequency_dict.items():
            while len(result) < frequency:
                result.append([])

            for index in range(frequency):
                result[index].append(num)
        
        return result
