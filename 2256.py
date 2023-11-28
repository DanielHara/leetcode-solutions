# Question 2256: https://leetcode.com/problems/minimum-average-difference/

"""
    Not a difficult question, just use some DP.
"""

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        S = []

        for num in nums:
            S.append(num + (S[-1] if S else 0))

        best_index = None
        best_average_difference = None
        for i in range(0, len(nums)):
            first_average_difference = S[i] // (i + 1)
            last_average_difference = (S[-1] - S[i]) // (len(nums) - i - 1) if (len(nums) - i - 1) > 0 else 0

            average_difference = abs(first_average_difference - last_average_difference)

            if best_index is None:
                best_index = i
                best_average_difference = average_difference
            elif average_difference < best_average_difference:
                best_index = i
                best_average_difference = average_difference

        return best_index
