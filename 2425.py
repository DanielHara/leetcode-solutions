"""
Question 2425: https://leetcode.com/problems/bitwise-xor-of-all-pairings/

Very interesting question! Just use the fact that x ^ x is always 0.
"""

class Solution:
    def getXORFromArray(self, array: List[int]) -> int:
        result = 0

        for num in array:
            result = result ^ num
        
        return result

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return 0

        if len(nums1) % 2 == 0 and len(nums2) % 2 == 1:
            return self.getXORFromArray(nums1)

        if len(nums1) % 2 == 1 and len(nums2) % 2 == 0:
            return self.getXORFromArray(nums2)

        return self.getXORFromArray(nums1 + nums2)
