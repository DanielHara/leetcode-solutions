"""
    Question 2542: https://leetcode.com/problems/maximum-subsequence-score/

    Very interesting question! One really nice trick to solve this question is to create a new nums array, as
    [nums1[i], nums2[i]]. After thinking a bit will notice that the order of the elements in this array actually doesn't matter.

    Then, order it by nums2[i], and you'll see the result is the best multiplication you can find of:
    nums2[i] and (the sum of the k largest elements in the array nums1[i:]).
"""

import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = []
        for i in range(len(nums1)):
            nums.append([nums1[i], nums2[i]])

        N = len(nums)

        nums.sort(key=lambda el: el[1])

        heap = []
        s = 0
        for i in range(N - k, N):
            s = s + nums[i][0]
            heapq.heappush(heap, nums[i][0])

        result = s * nums[N - k][1]

        for index in range(N - k - 1, -1, -1):
            if nums[index][0] > heap[0]:
                element = heapq.heappop(heap)
                s = s - element

                heapq.heappush(heap, nums[index][0])
                s = s + nums[index][0]

            result = max(result, s * nums[index][1])

        return result
