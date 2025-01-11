"""
    Question 2597: https://leetcode.com/problems/the-number-of-beautiful-subsets/

    The constraints are low: 1 <= nums.length <= 20
    So, you can just brute-force and build all the subsets which don't contain any pairs whose absolute
    different is k.
"""

class Solution:
    def buildBeautifulSubsets(self, start_index: int, k: int):
        if start_index == len(self.nums) - 1:
            self.result = self.result + 1
            return [set([self.nums[start_index]])]
        
        forward_sets = self.buildBeautifulSubsets(start_index + 1, k)
        start = self.nums[start_index]

        returned_list = [set([self.nums[start_index]])]
        self.result = self.result + 1
        for forward_set in forward_sets:
            returned_list.append(forward_set)
            if (self.nums[start_index] + k) not in forward_set and (self.nums[start_index] - k) not in forward_set:
                self.result = self.result + 1
                new_forward_set = forward_set.copy()
                new_forward_set.add(self.nums[start_index])
                returned_list.append(new_forward_set)
 
        return returned_list
    
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.result = 0
        number_beautiful_subsets = self.buildBeautifulSubsets(0, k)

        return self.result
