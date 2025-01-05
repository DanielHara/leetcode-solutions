# Question 553: https://leetcode.com/problems/optimal-division/

"""
    Just do it greedily!

    The first element doesn't matter, you always have to include it. As in the constraints you only have numbers >=2, you can optimally
    get the largest number just by always dividing the denominator of the fraction and making it as small as possible.
"""

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        
        if len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])

        array = nums[1:]
        array_string = []
        for num in array:
            array_string.append(str(num))
        
        return str(nums[0]) + '/' + '(' + '/'.join(array_string) + ')'
