# Question 977: https://leetcode.com/problems/squares-of-a-sorted-array/

# An O(N) rather than O(N log N) solution.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [None for i in range(len(nums))]

        start = 0
        end = len(nums) - 1

        count = 0
        while start < end:
            if abs(nums[start]) > abs(nums[end]):
                result[len(nums) - 1 - count] = nums[start] ** 2
                start = start + 1
            else:
                result[len(nums) - 1 - count] = nums[end] ** 2
                end = end - 1
            count = count + 1
        

        # They're equal
        result[0] = nums[start] ** 2

        return result
