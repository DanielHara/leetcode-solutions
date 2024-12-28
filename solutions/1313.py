# Question 1313: https://leetcode.com/problems/decompress-run-length-encoded-list/

"""
    Trivial question
"""

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed_list = []

        for i in range(0, len(nums), 2):
            frequency = nums[i]
            val = nums[i + 1]

            for repeat in range(frequency):
                decompressed_list.append(val)
        
        return decompressed_list
