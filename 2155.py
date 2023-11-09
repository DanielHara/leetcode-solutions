# Question 2155: https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

"""
    Fairly easy question. Just use some DP to do the trick
"""

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        number_of_1s_right = 0

        for num in nums:
            if num == 1:
                number_of_1s_right = number_of_1s_right + 1

        best_indices = [0]
        best_score = number_of_1s_right
        number_of_0s_left = 0

        for index in range(0, len(nums)):
            if nums[index] == 0:
                number_of_0s_left = number_of_0s_left + 1
            else:
                number_of_1s_right = number_of_1s_right - 1
            
            division_score = number_of_0s_left + number_of_1s_right
            if division_score == best_score:
                best_indices.append(index + 1)
            elif division_score > best_score:
                best_indices = [index + 1]
                best_score = division_score

        return best_indices
