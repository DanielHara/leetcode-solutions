# Question 2233: https://leetcode.com/problems/maximum-product-after-k-increments/

"""
    I got the following insight: say have a sorted array: [1,3,6,10,12]
    The best chance of getting a larger product is always to increment the smallest number.
    Then proceed as follows:

    [1,3,6,10,12] -> [3,3,6,10,12] -> [6,6,6,10,12] -> [10,10,10,10,12]

    and so on, until you run out of moves.

    After reaching a point you don't have moves anymore, just distribute it evenly from the left until
    the last element you have visited.

    If you visited all elements and still have most, just distribute it evenly.

    After all this, just compute the product of the numbers your got!
"""

class Solution:
    def calculateResult(self, nums: List[int]) -> int:
        result = 1
        mod = 10 ** 9 + 7
        
        for num in nums:
            result = ((result % mod) * (num % mod)) % mod
        return result
    
    def maximumProduct(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        diffs = []
        for i in range(len(nums) - 1):
            diffs.append(nums[i+1] - nums[i])
        
        i = 0
        while i < len(diffs):
            if k >= (i + 1) * diffs[i]:
                k = k - (i + 1) * diffs[i]
                i = i + 1
            else:
                break
        
        for j in range(i + 1 - 1):
            nums[j] = nums[i + 1 - 1]
        
        increment = k // (i + 1)
        rest = k % (i + 1)
        
        for j in range(i + 1):
            nums[j] = nums[j] + increment
            
        for j in range(rest):
            nums[j] = nums[j] + 1
        
        # Return the multiplication
        return self.calculateResult(nums)
