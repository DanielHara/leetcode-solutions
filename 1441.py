# Question 1441: https://leetcode.com/problems/build-an-array-with-stack-operations/

"""
    Fairly easy question, actually.
"""

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []

        target = [0] + target

        for i in range(1, len(target)):
            for j in range(0, target[i] - target[i - 1] - 1):
                result.append('Push')
                result.append('Pop')
            
            result.append('Push')

        return result
