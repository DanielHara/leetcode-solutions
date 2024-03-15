# Question 27: https://leetcode.com/problems/remove-element/

"""
    Really nice easy question!
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end_pointer = len(nums) - 1
        while end_pointer >= 0 and nums[end_pointer] == val:
            end_pointer = end_pointer - 1

        for pointer in range(len(nums)):
            if pointer > end_pointer:
                break
            
            if nums[pointer] == val:
                nums[pointer] = nums[end_pointer]
                end_pointer = end_pointer - 1
            
                while end_pointer >= 0 and nums[end_pointer] == val:
                    end_pointer = end_pointer - 1

            pointer = pointer + 1
        
        return end_pointer + 1
