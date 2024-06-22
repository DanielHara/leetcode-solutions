# Question 2772: https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/

"""
    Very interesting question! Do it greedily.
"""

class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        increase_balances = [0 for i in range(len(nums))]

        balance = 0
        for i in range(len(nums)):
            balance = balance + increase_balances[i]
            element = balance + nums[i]
            if element < 0:
                return False
            
            if element > 0 and i > len(nums) - k:
                return False

            balance = balance - element
            increase_balance_index = i + k
            if increase_balance_index < len(nums):
                increase_balances[increase_balance_index] = increase_balances[increase_balance_index] + element
        
        return True
