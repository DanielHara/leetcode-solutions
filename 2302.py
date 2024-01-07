"""
    Question 2302: https://leetcode.com/problems/count-subarrays-with-score-less-than-k/description/

    Nothing fancy, just use a prefix array and binary search. Another Hard question that should be 
    actually labelled Medium.
"""

class Solution:
    def getScore(self, i: int, j: int):
        return (self.S[j] - (self.S[i - 1] if i - 1 >= 0 else 0)) * (j - i + 1)
    
    def binarySearch(self, start: int, end: int, i: int, k: int):
        if start > end:
            return None
        
        half = (start + end) // 2

        if self.getScore(i, half) < k and (half == end or self.getScore(i, half + 1) >= k):
            return half
        
        if self.getScore(i, half) < k:
            return self.binarySearch(half + 1, end, i, k)
        
        return self.binarySearch(start, half - 1, i, k)

    
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Calculate prefix sum:

        self.S = []
        for num in nums:
            self.S.append(num + (self.S[-1] if self.S else 0))

        result = 0
        for i in range(len(self.S)):
            limit_index = self.binarySearch(i, len(self.S) - 1, i, k)

            if limit_index is not None:
                result = result + limit_index - i + 1

        return result
