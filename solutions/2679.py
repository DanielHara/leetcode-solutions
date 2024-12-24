# Question 2679: https://leetcode.com/problems/sum-in-a-matrix/

"""
    Just do it with a heap, no secrets involved.
"""

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        heaps = []
        for row in nums:
            heap = []
            for element in row:
                heapq.heappush(heap, -1 * element)

            heaps.append(heap)

        number_columns = len(nums[0])
        score = 0
        
        for repeat in range(number_columns):
            highest_number = 0
            for heap in heaps:
                popped_element = heapq.heappop(heap)
                highest_number = max(highest_number, (-1) * popped_element)

            score = score + highest_number
        
        return score
