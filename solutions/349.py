# Question 349: https://leetcode.com/problems/intersection-of-two-arrays/

# Trivial question, just use sets.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        for num in nums1:
            set1.add(num)
        
        set2 = set()
        for num in nums2:
            set2.add(num)
        
        result_set = set()
        for num in set1:
            if num in set2:
                result_set.add(num)
        
        for num in set2:
            if num in set1:
                result_set.add(num)
        
        return list(result_set)
            
        
        
        
        
        