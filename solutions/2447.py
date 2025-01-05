"""
    Question 2447: https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

    This question is similar to question 2470: https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/,
    whith the difference that you may not brute-force finding the GCD. You should instead use a smarter algorithm, like the Euclidean algorithm.
"""

class Solution:
    def getGCD(self, a: int, b: int):
        if b > a:
            temp = b
            b = a
            a = temp

        while b > 0:
            temp = b
            b = a % b
            a = temp
        
        return a

    def subarrayGCD(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(0, len(nums)):
            gcd = nums[i]
            for j in range(i, len(nums)):
                gcd = self.getGCD(gcd, nums[j])
                if gcd == k:
                    result = result + 1
                elif gcd < k:
                    break

        return result
