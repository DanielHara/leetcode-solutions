# Question 1375: https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

# A very interesting question!

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        result = 0

        maximum = None
        for index, element in enumerate(flips):
            maximum = max(maximum, element) if maximum is not None else element

            if maximum == index + 1:
                result = result + 1
        
        return result
