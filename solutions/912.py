# Question 912: https://leetcode.com/problems/sort-an-array/

# Nice warm-up question to repeat basic stuff, just classical merge sort

class Solution:
    def mergeSort(self, start, end, nums: List[int]):
        if start >= end:
            return

        half = (start + end) // 2

        self.mergeSort(start, half, nums)
        self.mergeSort(half + 1, end, nums)

        temp = []
        first_half_index = start
        second_half_index = half + 1

        while first_half_index <= half and second_half_index <= end:
            if nums[first_half_index] <= nums[second_half_index]:
                temp.append(nums[first_half_index])
                first_half_index = first_half_index + 1
            else:
                temp.append(nums[second_half_index])
                second_half_index = second_half_index + 1
        
        while first_half_index <= half:
            temp.append(nums[first_half_index])
            first_half_index = first_half_index + 1

        while second_half_index <= end:
            temp.append(nums[second_half_index])
            second_half_index = second_half_index + 1
        
        for copy_index in range(start, end + 1):
            nums[copy_index] = temp[copy_index - start]

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(0, len(nums) - 1, nums)
        
        return nums

