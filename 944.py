# Question 944: https://leetcode.com/problems/delete-columns-to-make-sorted/

"""
    Trivial question
"""

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0

        for column in range(0, len(strs[0])):
            for index in range(len(strs) - 1):
                if strs[index][column] > strs[index + 1][column]:
                    result = result + 1
                    break
        
        return result
