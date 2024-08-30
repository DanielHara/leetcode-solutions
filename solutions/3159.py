# Question 3159: https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

"""
    Just build an array with the indexes. Trivial question, really
"""

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        indices = []

        for index, num in enumerate(nums):
            if num == x:
                indices.append(index)
        
        answer = []
        for query in queries:
            if query - 1 < len(indices):
                answer.append(indices[query - 1])
            else:
                answer.append(-1)

        return answer
