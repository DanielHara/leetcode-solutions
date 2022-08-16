"""
Question 1577: https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/
"""

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # The order doesn't matter, so we can transform both arrays into frequency_dict:
        
        frequency_dict_1 = {}
        for num in nums1:
            frequency_dict_1[num] = frequency_dict_1.get(num, 0) + 1
        
        
        frequency_dict_2 = {}
        for num in nums2:
            frequency_dict_2[num] = frequency_dict_2.get(num, 0) + 1
        
        
        result = 0
        for i in range(len(nums1)):
            squared = nums1[i] ** 2

            for j in frequency_dict_2:
                if squared % j == 0:
                    searched = squared // j
                
                    if searched == j:
                        result = result + (frequency_dict_2[j] * (frequency_dict_2[j] - 1)) // 2
                    elif searched < j:
                        result = result + (frequency_dict_2[j] * frequency_dict_2.get(searched, 0))
        
                                       
        for i in range(len(nums2)):
            squared = nums2[i] ** 2

            for j in frequency_dict_1:
                if squared % j == 0:
                    searched = squared // j
                
                    if searched == j:
                        result = result + (frequency_dict_1[j] * (frequency_dict_1[j] - 1)) // 2
                    elif searched < j:
                        result = result + frequency_dict_1[j] * frequency_dict_1.get(searched, 0)
        
        return result
