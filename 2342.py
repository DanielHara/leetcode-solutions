# Question 2342: https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

"""
    Not a difficult question, just use hashmap, and the sum of the digits and the key.
"""

class Solution:
    def get_digit_sum(self, num: int) -> int:
        result = 0
        
        while num > 0:
            result = result + num % 10
            num = num // 10

        return result

    def maximumSum(self, nums: List[int]) -> int:
        sum_digits_to_heap = {}

        for index, num in enumerate(nums):
            digit_sum = self.get_digit_sum(num)

            if digit_sum not in sum_digits_to_heap:
                sum_digits_to_heap[digit_sum] = []
            
            heap = sum_digits_to_heap[digit_sum]
            heapq.heappush(heap, (-1 * num, index))
        
        result = -1
        for index, num in enumerate(nums):
            digit_sum = self.get_digit_sum(num)
            heap = sum_digits_to_heap[digit_sum]

            if heap[0][1] != index:
                result = max(result, num + (-1 * heap[0][0]))
            elif len(heap) >= 2:
                element = heapq.heappop(heap)
                result = max(result, num + (-1 * heap[0][0]))
                heapq.heappush(heap, element)

        return result

