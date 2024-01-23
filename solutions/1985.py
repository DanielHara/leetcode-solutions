# Question 1985: https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

"""
    I have no idea why this question is rated as medium, because this very simple solution passes the judge.
"""

class Solution:
    def compare(self, num1: str, num2: str) -> int:
        if len(num1) < len(num2):
            return -1
        
        if len(num1) > len(num2):
            return 1
        
        for i in range(len(num1)):
            if num1[i] < num2[i]:
                return -1
            
            if num1[i] > num2[i]:
                return 1

        return 0

    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=functools.cmp_to_key(self.compare), reverse=True)

        return nums[k - 1]
