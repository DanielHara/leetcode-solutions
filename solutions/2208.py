# Question 2208: https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

"""
    Not a difficult question. Just do it greedily, and use a heap to speed up the process in order
    to quickly find the largest element in the array.
"""

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)

        heap = []   
        for num in nums:
            heapq.heappush(heap, -1 * num)

        result = 0
        current_sum = total_sum
        while current_sum > total_sum / 2:
            negative_element = heapq.heappop(heap)
            element = -1 * negative_element

            half = element / 2
            current_sum = current_sum - half

            heapq.heappush(heap, -1*half)

            result = result + 1

        return result
