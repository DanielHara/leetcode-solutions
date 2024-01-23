"""
    Question 2461: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k

    Use some manipulation with a dictionary and set to solve this question in O(N) time.
"""

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        exceeding_frequency_dict = {}
        distinct_set = set()

        end = k
        
        s = 0
        for index in range(end):
            number = nums[index]
            if number in distinct_set:
                exceeding_frequency_dict[number] = exceeding_frequency_dict.get(number, 0) + 1

            distinct_set.add(number)
            s = s + number
        
        result = 0
        if not exceeding_frequency_dict:
            result = max(result, s)
        
        for index in range(end, len(nums), 1):
            number_to_delete = nums[index - k]
            s = s - number_to_delete

            if number_to_delete in exceeding_frequency_dict:
                if exceeding_frequency_dict[number_to_delete] <= 1:
                    del exceeding_frequency_dict[number_to_delete]
                else:
                    exceeding_frequency_dict[number_to_delete] = exceeding_frequency_dict[number_to_delete] - 1
            else:
                if number_to_delete in distinct_set:
                    distinct_set.remove(number_to_delete)

            number = nums[index]
            s = s + number
            
            if number in distinct_set:
                exceeding_frequency_dict[number] = exceeding_frequency_dict.get(number, 0) + 1
            distinct_set.add(number)

            if not exceeding_frequency_dict:
                result = max(result, s)

        return result
