"""
    Question 2602: https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

    Just use a prefix-sum to get it fast!
    Get nums and query sorted, it helps!
"""

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        S = []
        for num in nums:
            S.append(S[-1] + num if S else num)
        
        queries = list(enumerate(queries))
        queries.sort(key=lambda query: query[1])

        answer = [None for i in range(len(queries))]

        nums_index = 0
        for [query_index, query_value] in queries:
            while nums_index < len(nums) and nums[nums_index] < query_value:
                nums_index = nums_index + 1

            left_part = (-(S[nums_index - 1] if nums_index - 1 >= 0 else 0) + nums_index * query_value)
            right_part = (S[-1] - (S[nums_index - 1] if nums_index - 1 >= 0 else 0) - query_value * (len(nums) - nums_index))

            query_result = left_part + right_part
            answer[query_index] = query_result

        return answer
