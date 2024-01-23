# Question 1567: https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

"""
    Just create an array of tokens splitting by 0 (an array which contains zero cannot have its product great than zero),
    and get the largest array which has an even number of negative numbers to search for the answer.
"""

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # First, get an array splliting nums by 0:

        tokens = []
        
        i = 0
        while i < len(nums):
            j = i
            while j < len(nums) and nums[j] != 0:
                j = j + 1
            
            tokens.append(nums[i: j])
            i = j + 1

        result = 0
        for array in tokens:
            count_negative_numbers = 0
            lowest_index = None 
            highest_index = None

            for index, number in enumerate(array):
                if number < 0:
                    count_negative_numbers = count_negative_numbers + 1
                
                    if lowest_index is None:
                        lowest_index = index

                    highest_index = index
            
            if count_negative_numbers % 2 == 0:
                result = max(result, len(array))
            else:
                result = max(result, len(array) - lowest_index - 1, highest_index)   


        return result
