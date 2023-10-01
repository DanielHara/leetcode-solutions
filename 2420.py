"""
Question 2420: https://leetcode.com/problems/find-all-good-indices

This question is very similar to question 2100 (https://leetcode.com/problems/find-good-days-to-rob-the-bank/), so
I just changed the approach a bit.

"""

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)

        S = [None for i in range(N)]
        S[-1] = 0
        S[len(nums) - 2] = 1

        for i in range(N - 3, -1, -1):
            if nums[i + 1] <= nums[i + 2]:
                S[i] = 1 + S[i + 1]
            else:
                S[i] = 1
        
        T = [None for i in range(N)]
        T[0] = 0
        T[1] = 1

        for i in range(2, N, 1):
            if nums[i - 2] >= nums[i - 1]:
                T[i] = 1 + T[i - 1]
            else:
                T[i] = 1
        
        result = []
        for i in range(N):
            if S[i] >= k and T[i] >= k:
                result.append(i)
        
        return result
