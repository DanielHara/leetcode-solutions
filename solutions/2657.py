# Question 2657: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

"""
    A trivial O(N**2) solution should be enough, as 1 <= A.length == B.length == n <= 50
"""

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        frequency_dict_A = {}
        frequency_dict_B = {}

        result = []
        for i in range(len(A)):
            frequency_dict_A[A[i]] = frequency_dict_A.get(A[i], 0) + 1
            frequency_dict_B[B[i]] = frequency_dict_B.get(B[i], 0) + 1

            s = 0
            for element in frequency_dict_A:
                s = s + min(frequency_dict_A[element], frequency_dict_B.get(element, 0))
            result.append(s)
        
        return result
