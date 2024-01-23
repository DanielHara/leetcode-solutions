# Question 1238: https://leetcode.com/problems/circular-permutation-in-binary-representation/

"""
    A relatively easy question if you know how to generate Gray codes: https://en.wikipedia.org/wiki/Gray_code
"""


class Solution:
    def generateGrayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        
        previous = self.generateGrayCode(n - 1)
        
        answer = previous
        
        for el in reversed(previous):
            answer.append(2**(n - 1) + el)
        
        return answer

    def circularPermutation(self, n: int, start: int) -> List[int]:
        grayCodes = self.generateGrayCode(n)

        start_index = 0
        while grayCodes[start_index] != start:
            start_index = start_index + 1
        
        answer = grayCodes[start_index:] + grayCodes[0: start_index]

        return answer
