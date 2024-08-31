# Question 2375: https://leetcode.com/problems/construct-smallest-number-from-di-string/

"""
    Just use backtracking! Try all the possibilities, and give up if you came to a point where there's no exit.
"""

class Solution:
    def findSmallestNumberGivenStart(self, start, pattern, used_digits):
        if not pattern:
            return [str(start)]
        
        direction = pattern[0]

        if direction == 'I':
            if start == 9:
                return None

            for possible_digit in range(start + 1, 10, 1):
                if possible_digit not in used_digits:
                    copy_used_digits = used_digits.copy()
                    copy_used_digits.add(possible_digit)
                    possibility = self.findSmallestNumberGivenStart(possible_digit, pattern[1:], copy_used_digits)
                    if possibility:
                        return [str(start)] + possibility
        else:
            if start == 1:
                return None
            for possible_digit in range(1, start, 1):
                if possible_digit not in used_digits:
                    copy_used_digits = used_digits.copy()
                    copy_used_digits.add(possible_digit)
                    possibility = self.findSmallestNumberGivenStart(possible_digit, pattern[1:], copy_used_digits)
                    if possibility:
                        return [str(start)] + possibility
    
            
        return None

    def smallestNumber(self, pattern: str) -> str:
        for digit in range(1, 10):
            possibility = self.findSmallestNumberGivenStart(digit, pattern, set([digit]))
            if possibility:
                return ''.join(possibility)
