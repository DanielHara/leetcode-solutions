# Question 3097: https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

"""
    For this question, I've had to look at the hints. The hint which says:
        So the number of different results for each nums[i] is at most the number of bits 32.
    solves the question. Difficult to come to it in an interview, though
"""

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        accumulated_ors_list = []

        accumulated_ors_list.append({nums[0]: 1})
        for i in range(1, len(nums)):
            previous_accumulated_ors = accumulated_ors_list[-1]

            current_accumulated_ors = {nums[i]: 1}
            for [previous_accumulated_or, previous_length] in previous_accumulated_ors.items():
                accumulated_or = previous_accumulated_or | nums[i]
                if accumulated_or not in current_accumulated_ors:
                    current_accumulated_ors[accumulated_or] = 1 + previous_length
            
            accumulated_ors_list.append(current_accumulated_ors)

        result = None
        for accumulated_ors in accumulated_ors_list:
            for [accumulated_or, length] in accumulated_ors.items():
                if accumulated_or >= k:
                    result = min(result, length) if result is not None else length

        return result if result is not None else -1
