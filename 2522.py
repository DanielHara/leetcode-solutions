"""
Question 2522: https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

A DP approach does the trick
"""


class Solution:
    def getPositions(self, num: List[int]) -> set:
        result_set = set()
        count = 0
        while num > 0:
            if num % 2 != 0:
                result_set.add(count)

            count = count + 1
            num = num // 2
        
        return result_set
    
    
    def longestNiceSubarray(self, nums: List[int]) -> int:
        accumulated_set = self.getPositions(nums[0])

        j = 0
        i = 1
        result = 1

        while i < len(nums) and j < len(nums):
            invalid_set = None

            while i < len(nums):
                new_element = nums[i]
                new_positions = self.getPositions(new_element)
                
                invalid_set = set()

                is_invalid = False
                for new_position in new_positions:
                    if new_position in accumulated_set:
                        is_invalid = True
                        invalid_set.add(new_position)
                
                if is_invalid:
                    break
                else:
                    for position in new_positions:
                        accumulated_set.add(position)
                    i = i + 1
                    result = max(result, i - j)
            
            while j < len(nums) and invalid_set:
                removed_element = nums[j]
                removed_positions = self.getPositions(nums[j])

                for position in removed_positions:
                    accumulated_set.remove(position)
                    if position in invalid_set:
                        invalid_set.remove(position)
                
                j = j + 1
        
        return result

