# Question 1712: https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

"""
    Just use a lot of binary search so that you get a O(N * log(N)) solution. As the boundaries are nums.length <= 10**5,
    a worse time complexity will probably not pass.
"""

class Solution:
    # Find the lowest index for which array[index] >= target
    def binarySearch1(self, start: int, end: int, array: List[int], target: int):
        if start > end:
            return None

        half = (start + end) // 2
        if array[half] >= target and (half == start or array[half - 1] < target):
            return half
        if array[half] >= target:
            return self.binarySearch1(start, half - 1, array, target)
        return self.binarySearch1(half + 1, end, array, target)
    
    # Find the highest index for which array[index] <= target
    def binarySearch2(self, start: int, end: int, array: List[int], target: int):
        if start > end:
            return None
        
        half = (start + end) // 2
        if array[half] <= target and (half == end or array[half + 1] > target):
            return half
        if array[half] <= target:
            return self.binarySearch2(half + 1, end, array, target)
        return self.binarySearch2(start, half - 1, array, target)

    def waysToSplit(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        
        S = [nums[0]]

        for i in range(1, len(nums)):
            S.append(S[-1] + nums[i])
        
        result = 0
        for i in range(0, len(nums) - 2):
            # find smallest j between i + 1 and len(nums) - 2 (inclusive) for which S[j] - S[i] >= S[i]
            j = self.binarySearch1(i + 1, len(nums) - 2, S, 2 * S[i])

            if j is None:
                return result
            
            # find highest k between j and len(nums) - 2 (inclusive) for which S[k] - S[i] <= S[-1] - S[k]
            target = (S[-1] + S[i]) // 2
            k = self.binarySearch2(j, len(nums) - 2, S, target)

            if k is None:
                continue
            
            result = (result + (k - j + 1) % mod) % mod
        
        return result
