"""
    Question 2470: https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

    I just brute-forced it, and the solution got accepted. Interesting. It works because the boundaries for nums[i] are low.
"""

class Solution:
    def getLCM(self, a: int, b: int):
        maximum = max(a, b)
        multiple = 1

        lcm = maximum
        while lcm % a != 0 or lcm % b != 0:
            multiple = multiple + 1
            lcm = multiple * maximum
        
        return lcm
    
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(0, len(nums)):
            lcm = 1
            for j in range(i, len(nums)):
                lcm = self.getLCM(lcm, nums[j])
                if lcm == k:
                    result = result + 1
                elif lcm > k:
                    break

        return result
