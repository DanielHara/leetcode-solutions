# Question 992: https://leetcode.com/problems/subarrays-with-k-different-integers/

"""
    Another sliding window problem. From a start point, just go to the index end1, up from which where you find exactly k distinct integers.
    From this index, set index end2, up to which you still just get repeated integers.
    Then, just get the length (end2 - end1 + 1), and sum it to the result
"""

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        start = 0
        end1 = 0
        end2 = 0

        frequency_dict = {}
        frequency_dict[nums[0]] = 1

        result = 0
        while start < len(nums):
            while end1 < len(nums) and len(frequency_dict) < k:
                if end1 < len(nums) - 1:
                    frequency_dict[nums[end1 + 1]] = frequency_dict.get(nums[end1 + 1], 0) + 1
                end1 = end1 + 1
            
            end2 = max(end2, end1)
            while end2 < len(nums) - 1 and nums[end2 + 1] in frequency_dict:
                end2 = end2 + 1

            if len(frequency_dict) == k:
                result = result + end2 - end1 + 1

            frequency_dict[nums[start]] = frequency_dict[nums[start]] - 1
            if frequency_dict[nums[start]] == 0:
                del frequency_dict[nums[start]]

            start = start + 1

        return result
