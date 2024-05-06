"""
    Question 2537: https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

    This question is quite cool! I used a sliding-window approach to solve it.
"""

class Solution:
    def countGood(self, nums, k):
        start = 0
        end = 0
        frequency_dict = {}

        result = 0
        N = len(nums)
        number_pairs = 0
        while start < N:
            while end < N and number_pairs < k:
                frequency = frequency_dict.get(nums[end], 0)
                number_pairs = number_pairs - frequency * (frequency - 1) // 2

                frequency = frequency + 1
                frequency_dict[nums[end]] = frequency
                number_pairs = number_pairs + frequency * (frequency - 1) // 2
                
                end = end + 1

            if number_pairs >= k:
                result = result + (N - end + 1)
            else:
                return result

            frequency = frequency_dict.get(nums[start], 0)
            number_pairs = number_pairs - frequency * (frequency - 1) // 2

            frequency = frequency - 1
            frequency_dict[nums[start]] = frequency 
            if frequency_dict[nums[start]] == 0:
                del frequency_dict[nums[start]]
            
            number_pairs = number_pairs + frequency * (frequency - 1) // 2

            start = start + 1

        return result                
