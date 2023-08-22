"""
Question 1630: https://leetcode.com/problems/arithmetic-subarrays/
"""

"""
    Looking at the constraints of the problem, the array will have at most 500 elements, which makes a O(N**2) feasible.
"""


class Solution:
    def isArithmetic(self, array: List[int]) -> bool:
        if not array or len(array) <= 1:
            return False

        diff = array[1] - array[0]
        for i in range(1, len(array) - 1, 1):
            if array[i + 1] - array[i] != diff:
                return False
        
        return True

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []

        for i in range(len(l)):
            start = l[i]
            end = r[i]

            array = nums[start: end + 1]
            array.sort()

            answer.append(self.isArithmetic(array))

        return answer
