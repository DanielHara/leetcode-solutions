# Question 2090: https://leetcode.com/problems/k-radius-subarray-averages/

"""
    Quite trivial question, just use prefix sum
"""

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        S = []
        for num in nums:
            S.append(num + (S[-1] if S else 0))
        
        answer = []
        for index in range(len(nums)):
            if index + k >= len(nums) or index - k - 1 < -1:
                answer.append(-1)
                continue
 
            average = (S[index + k] - (S[index - k - 1] if index - k - 1 >= 0 else 0)) // (2 * k + 1)
            answer.append(average)

        return answer
