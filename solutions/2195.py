# Question 2195: https://leetcode.com/problems/append-k-integers-with-minimal-sum/

"""
    Just do it greedily and take care so that the solution is O(N), and not O(K), because the upperbound of k is too large.
"""

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums_set = set()
        for num in nums:
            nums_set.add(num)

        S = k * (k + 1) // 2
        rest_numbers = 0
        sum_to_exclude = 0
        for num in nums_set:
            if num <= k:
                sum_to_exclude = sum_to_exclude + num
                rest_numbers = rest_numbers + 1

        result = S - sum_to_exclude
        index = k + 1
        while rest_numbers > 0:
            if index not in nums_set:
                result = result + index
                rest_numbers = rest_numbers - 1
            index = index + 1

        return result
