# Question 2024: https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

"""
    Just use a sliding window approach, scanning the array twice.
"""

class Solution:
    def findPartialResult(self, answerKey: str, k: int, is_from_T_to_F: bool) -> int:
        from_char = 'T' if is_from_T_to_F else 'F'
        to_chart = 'F' if is_from_T_to_F else 'T'

        i = 0
        result = 0

        used = 0
        j = i
        while i < len(answerKey):
            while j < len(answerKey) and used < k:
                if answerKey[j] == from_char:
                    j = j + 1
                else:
                    used = used + 1
                    j = j + 1

            while j < len(answerKey) and answerKey[j] == from_char:
                j = j + 1

            result = max(result, j - i)

            while i < len(answerKey) and answerKey[i] == from_char:
                i = i + 1

            if i < len(answerKey) and answerKey[i] == to_chart:
                used = used - 1
                i = i + 1

        return result


    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # Use sliding window twice:

        # First, from 'T' to 'F':
        # find the first one in answerKey where answerKey[i] == 'T':

        return max(self.findPartialResult(answerKey, k, True), self.findPartialResult(answerKey, k, False))
