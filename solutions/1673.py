# Question 1673: https://leetcode.com/problems/find-the-most-competitive-subsequence/

"""
   You could solve this problem in a greedy way:
   Put the numbers in a stack, as long as they are non-decreasing. If you find a number that's smaller than the top of stack,
   you could make a more competitive sequence by popping from the stack until the top of the stack is a number smaller or equal than
   the number you're processing. Keep doing this until you have used up your quota of numbers to remove.
"""

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        result = []
        
        number_elements_remove = len(nums) - k
        while nums:
            num = nums.pop(0)
            
            while number_elements_remove > 0 and result and result[-1] > num:
                result.pop()
                number_elements_remove = number_elements_remove - 1
            result.append(num)
        
        return result[0:k]
