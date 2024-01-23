# Question 1968: https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

"""
  A zig-zag array will do, in which nums[i] < nums[i+1] > nums[i+2], and so on. That way it's impossible
  that an element is equal to the average of its neighbours. It's trivial to build a zig-zag array out of
  a sorted arra.y
"""

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        answer = []

        N = len(nums)

        for i in range(N // 2):
            answer.append(nums[i])
            answer.append(nums[N - 1 - i])
        
        if N % 2 != 0:
            answer.append(nums[N // 2])
        
        return answer
