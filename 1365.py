# Question 1365: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# Easy question

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = [nums[i], i]
        
        nums.sort(key=lambda el: el[0])

        result = [None for i in range(len(nums))]

        last_count = 0
        last = None
        for index, [value, i] in enumerate(nums):
            if last == value:
                result[i] = index - last_count
                last_count = last_count + 1
            else:
                last = value
                last_count = 1
                result[i] = index
        
        return result
