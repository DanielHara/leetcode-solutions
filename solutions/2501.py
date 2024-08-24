"""
    Question 2501: https://leetcode.com/problems/longest-square-streak-in-an-array/

    Just a bit of DP does the trick
"""

class Solution:
    def recursive_calculate_max_length(self, start):
        element = self.nums[start]
        index_of_squared = self.value_to_index_dict.get(element ** 2, None)

        if index_of_squared is None:
            self.dp[start] = 1
            return 1
        
        result = 1 + self.recursive_calculate_max_length(index_of_squared)
        self.dp[start] = result
        return result

    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        self.nums = nums

        self.dp = [None for i in range(len(nums))]

        self.value_to_index_dict = {}
        for index, num in enumerate(nums):
            if num not in self.value_to_index_dict:
                self.value_to_index_dict[num] = index

        for i in range(len(nums)):
            self.recursive_calculate_max_length(i)

        maximum = -1
        for length in self.dp:
            if length >= 2:
                maximum = max(maximum, length)

        return maximum
