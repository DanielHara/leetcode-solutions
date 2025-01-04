"""
    Question 2530: https://leetcode.com/problems/maximal-score-after-applying-k-operations/

    Easy question, just do it greedily and always pick the largest element in the array. Use a heap
    to do it fast.
"""

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, (-1* num, num))
        
        score = 0
        for _ in range(k):
            (negative_maximum_num, maximum_num) = heapq.heappop(heap)
            score = score + maximum_num

            replaced = maximum_num // 3 if maximum_num % 3 == 0 else maximum_num // 3 + 1
            heapq.heappush(heap, (-1* replaced, replaced))

        return score
