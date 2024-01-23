"""
Question 1658: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

You basically need to find an efficient way find i and j such that the sum(nums[0:i]) + sum(nums[j:]) is equal to x, and such that the
sum of the length of these both chunks is minimum. For this, you could keep a hash table so that you can query in constant time which index is necessary
for sum(nums[0:index]) to have value target, and go through the array backwards, always checking for this index, and saving the best result you can find.
"""

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if x == 0:
            return 0
        
        dictionary = {}
        dictionary[0] = -1
        N = len(nums)
        
        acc = 0
        for i in range(N):
            acc = acc + nums[i]
            dictionary[acc] = i
        

        result = -1
        
        if x in dictionary:
            result = dictionary[x] + 1
        
        acc = 0
        for i in range(N):
            acc = acc + nums[N - 1 - i]
            
            if (x - acc) in dictionary and dictionary[x - acc] < N - i - 1:
                result = min(result, i + 1 + dictionary[x - acc] + 1) if result >= 0 else (i + 1 + dictionary[x - acc] + 1)
        
        return result
