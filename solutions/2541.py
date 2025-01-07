"""
    Question 2541: https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

    Easy question, but quite cool!
    Just make a diff array, just knowing the diff is enough to solve the question!
"""

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        diff_array = []
        for index in range(len(nums1)):
            diff = nums1[index] - nums2[index]
            diff_array.append(diff)

        if k == 0:
            for diff in diff_array:
                if diff != 0:
                    return -1
            return 0

        result = 0
        s = 0
        for diff in diff_array:
            if diff % k != 0:
                return -1
            
            if diff > 0:    
                result = result + diff // k

            s = s + diff
        
        if s != 0:
            return -1

        return result
