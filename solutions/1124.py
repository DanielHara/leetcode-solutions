# Question 1124: https://leetcode.com/problems/longest-well-performing-interval/

"""
    A very interesting and tricky question. I just had to follow the hints.
"""

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        array = [1 if hour > 8 else - 1 for hour in hours]
        
        prefix_sums = [0]
        for element in array:
            prefix_sums.append(element + prefix_sums[-1])
        
        value_to_lowest_index_in_prefix_sum = {}
        for index, prefix_sum in enumerate(prefix_sums):
            if prefix_sum not in value_to_lowest_index_in_prefix_sum:
                value_to_lowest_index_in_prefix_sum[prefix_sum] = index

        result = 0
        for index, prefix_sum in enumerate(prefix_sums):
            if prefix_sum > 0:
                result = max(result, index)
            elif (prefix_sum - 1) in value_to_lowest_index_in_prefix_sum:
                result = max(result, index - value_to_lowest_index_in_prefix_sum[prefix_sum - 1])

        return result
