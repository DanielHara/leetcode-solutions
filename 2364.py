# Question 2364: https://leetcode.com/problems/count-number-of-bad-pairs/

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # Start by counting the number of pairs which are not bad (let's call them good pairs):
        # For a good pair: nums[j] - nums[i] == j - i holds, that is:
        # nums[j] - j == nums[i] - i holds.
        
        N_good_pairs = 0
        
        frequency_dict = {}
        
        for i, num in enumerate(nums):
            frequency_dict[num - i] = frequency_dict.get(num - i, 0) + 1
        
        for value in frequency_dict.values():
            N_good_pairs = N_good_pairs + (value * (value - 1)) // 2
            
        N = len(nums)
        
        return (N * (N - 1)) // 2 - N_good_pairs
