# Question 2149: https://leetcode.com/problems/rearrange-array-elements-by-sign/

"""
    An interesting, but not difficult question
"""

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        index_of_positive_number = 0
        
        while nums[index_of_positive_number] < 0:
            index_of_positive_number = index_of_positive_number + 1
        
        index_of_negative_number = 0
        while nums[index_of_negative_number] > 0:
            index_of_negative_number = index_of_negative_number + 1

        result = [None for i in range(len(nums))]

        i = 0
        while i < len(result):
            result[i] = nums[index_of_positive_number]
            i = i + 1
            
            index_of_positive_number = index_of_positive_number + 1
            while index_of_positive_number < len(result) and nums[index_of_positive_number] < 0:
                index_of_positive_number = index_of_positive_number + 1

            result[i] = nums[index_of_negative_number]
            i = i + 1
            index_of_negative_number = index_of_negative_number + 1

            while index_of_negative_number < len(result) and nums[index_of_negative_number] > 0:
                index_of_negative_number = index_of_negative_number + 1

        return result
