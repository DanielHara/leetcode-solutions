# Question 2239: https://leetcode.com/problems/find-closest-number-to-zero/

"""
    Very trivial, even stupid question. I don't know why it's on Leetcode :/
"""

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, (abs(num), num))
        
        if len(heap) >= 2:
            [abs_1, result] = heappop(heap)
            
            while heap and heap[0][0] == abs_1:
                [abs_2, num_2] = heappop(heap)
                result = max(result, num_2)

            return result

        return heap[0][1]
