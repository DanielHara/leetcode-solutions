# Question 1283: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

# Just binary-search for the answer!

class Solution:
    def isPossible(self, nums: List[int], divisor: int, threshold: int) -> bool:
        soma = 0
        for num in nums:
            soma = soma + (num // divisor if num % divisor == 0 else (num // divisor + 1))

        return soma <= threshold
    
    def binarySearch(self, nums: List[int], threshold: int, low: int, high: int):
        half = (low + high) // 2

        if low > high:
            return None

        possible = self.isPossible(nums, half, threshold) 
        if possible and (half == low or not self.isPossible(nums, half - 1, threshold)):
            return half
        if possible:
            return self.binarySearch(nums, threshold, low, half - 1)    
        return self.binarySearch(nums, threshold, half + 1, high)            

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = sum(nums)

        return self.binarySearch(nums, threshold, low, high)
