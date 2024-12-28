# Question 2615: https://leetcode.com/problems/sum-of-distances/

"""
    This is a very interesting question! Map the values to the indexes where they occur in the array, and
    just do an optimized calculation. Nothing really fancy.
"""

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        value_to_indexes_map = {}

        for index, num in enumerate(nums):
            if num not in value_to_indexes_map:
                value_to_indexes_map[num] = []

            value_to_indexes_map[num].append(index)
        
        arr = [0 for num in nums]

        for index_array in value_to_indexes_map.values():
            prefix_sum = []
            for element in index_array:
                prefix_sum.append(element + (prefix_sum[-1] if prefix_sum else 0))

            suffix_sum = []
            for element in reversed(index_array):
                suffix_sum.append(element + (suffix_sum[-1] if suffix_sum else 0))
            suffix_sum.reverse()

            for index, element in enumerate(index_array):
                if index + 1 < len(suffix_sum):
                    arr[element] = arr[element] + suffix_sum[index + 1] - (len(suffix_sum) - (index + 1)) * element
                if index - 1 >= 0:
                    arr[element] = arr[element] + (index) * element - prefix_sum[index - 1]

        return arr
