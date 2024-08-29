"""
    Question 2831: https://leetcode.com/problems/find-the-longest-equal-subarray/

    A very interesting question! Store the array of the indexes in a dictionary,
    and use a sliding window approach in every of the indexes array.
"""

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        num_to_indices = {}

        for index, num in enumerate(nums):
            if num not in num_to_indices:
                num_to_indices[num] = []
            
            num_to_indices[num].append(index)

        result = 1
        for indices in num_to_indices.values():
            start = 0
            end = 0

            number_differences = 0
            while start < len(indices):
                while end < len(indices) and number_differences <= k:
                    result = max(result, end - start + 1)

                    end = end + 1
                    if end < len(indices):
                        number_differences = number_differences + indices[end] - (indices[end - 1] if end - 1 >= 0 else 0) - 1

                if start < len(indices) - 1:
                    number_differences = number_differences - (indices[start + 1] - indices[start] - 1)
                else:
                    number_differences = 0
                start = start + 1

        return result
