# Question 2369: https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

class Solution:
    # Use dynamic programming to solve it!
    def validPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        
        # dp[i] saves the result for array nums[i:]
        dp = [False for i in range(N)]

        for i in range(N - 2, -1, -1):
            hasValidPartition = False

            if nums[i] == nums[i + 1]:
                hasValidPartition = hasValidPartition or (i + 2 >= N or dp[i + 2])
            
            if i + 2 < N and (nums[i] == nums[i + 1] and nums[i + 1] == nums[i + 2]):
                hasValidPartition = hasValidPartition or (i + 3 >= N or dp[i + 3])
            
            if i + 2 < N and (nums[i] + 1 == nums[i + 1] and nums[i + 1] + 1 == nums[i + 2]):
                hasValidPartition = hasValidPartition or (i + 3 >= N or dp[i + 3])
            
            dp[i] = hasValidPartition

        return dp[0]
