# Question 2653: https://leetcode.com/problems/sliding-subarray-beauty/

"""
    As -50 <= nums[i] <= 50, just brute-forcing is fine.
"""

class Solution:
    def getBeauty(self, frequencies: List[int], x: int):
        total = 0
        for index, frequency in enumerate(frequencies):
            total = frequency + total
            if total >= x:
                return index - 50
        
        return 0
    
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        limit = 50

        frequencies = [0 for i in range(limit)]
        for index in range(k):
            if nums[index] < 0:
                frequencies[nums[index] + limit] = frequencies[nums[index] + limit] + 1
        
        result = [self.getBeauty(frequencies, x)]

        for index in range(k, len(nums)):
            if nums[index - k] < 0:
                frequencies[nums[index - k] + limit] = frequencies[nums[index - k] + limit] - 1
            if nums[index] < 0:
                frequencies[nums[index] + limit] = frequencies[nums[index] + limit] + 1

            beauty = self.getBeauty(frequencies, x)
            result.append(beauty)

        return result
