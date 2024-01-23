# Question 1437: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

"""
    Trivial question
"""

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = 0
        while i < len(nums) and nums[i] == 0:
            i = i + 1

        while i < len(nums) - 1:
            j = i + 1
            
            while j < len(nums) and nums[j] == 0:
                j = j + 1
            
            if j < len(nums) and j - i - 1 < k:
                return False
            i = j
        
        return True
