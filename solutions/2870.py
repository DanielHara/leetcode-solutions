# Question 2870: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

"""
    Quite easy question
"""

class Solution:
    def minOperationsForFrequency(self, frequency: int):
        if frequency == 1:
            return None
        
        if frequency % 3 == 0:
            return frequency // 3
        
        if frequency % 3 == 1:
            return (frequency - 4) // 3 + 2
        
        if frequency % 3 == 2:
            return 1 + (frequency - 2) // 3
    
    def minOperations(self, nums: List[int]) -> int:
        frequency_dict = {}

        for num in nums:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1
        
        frequencies = frequency_dict.values()
        result = 0
        for frequency in frequencies:
            operations = self.minOperationsForFrequency(frequency)

            if operations is None:
                return -1

            result = result + operations
        
        return result
