"""
    Question 2606: https://leetcode.com/problems/find-the-substring-with-maximum-cost/

    Just a variation of question 53: https://leetcode.com/problems/maximum-subarray/, just use some DP
"""

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        char_to_value_dict = {}
        for index in range(ord('a'), ord('z') + 1, 1):
            char_to_value_dict[chr(index)] = index - ord('a') + 1
        for index in range(len(chars)):
            char_to_value_dict[chars[index]] = vals[index]

        nums = [char_to_value_dict[char] for char in s]
        dp = [None for index in range(len(nums))]
        dp[-1] = nums[-1]
        for index in range(len(nums) - 2, -1, -1):
            dp[index] = max(nums[index], nums[index] + dp[index + 1])

        return max(max(dp), 0)
