# Question 410: https://leetcode.com/problems/split-array-largest-sum/

"""
    Very interesting question!

    Try brute-force recursively with DP for the solution not to explode exponentially in time.
"""

class Solution:
    def recursiveSubArrays(self, start: int, k: int):
        key = str(start) + '_' + str(k)

        if key in self.dp:
            return self.dp[key]

        if k == 1:
            result = sum(self.nums[start:])
            self.dp[key] = result
            return result

        possibilities = []
        index = start
        s = 0

        while index <= len(self.nums) - k:
            s = s + self.nums[index]
            recursive = self.recursiveSubArrays(index + 1, k - 1)
            possibilities.append(max(recursive, s))
            if s > recursive:
                break
            index = index + 1
        
        result = min(possibilities)
        self.dp[key] = result
        return result

    def splitArray(self, nums: List[int], k: int) -> int:
        self.nums = nums

        self.dp = {}
        
        return self.recursiveSubArrays(0, k)
