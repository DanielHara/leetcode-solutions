# Question 744: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

"""
Trivial question
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        result = None

        for letter in letters:
            if letter > target:
                if result is None:
                    result = letter
                else:
                    if letter < result:
                        result = letter
        
        return result if result is not None else letters[0]
