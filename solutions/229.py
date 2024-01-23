"""
Question 229: https://leetcode.com/problems/majority-element-ii/

There's probably a very tricky solution with bit manipulation to do it in O(n) time and O(1), but I
haven't been able to figure it out (yet).
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency_dict = {}

        for num in nums:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1
        
        n = len(nums)
        answer = []
        for [key, value] in frequency_dict.items():
            if value > n // 3:
                answer.append(key)
        
        return answer
