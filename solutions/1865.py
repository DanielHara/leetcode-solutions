# Question 1865: https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

"""
    Use nums1 to iterate linearly, as its length is <= 1000, and use a frequency dict for nums2, which can have up to 10**5 elements
"""

class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        
        self.frequency_dict2 = {}
        
        self.nums2 = nums2
        for num in nums2:
            self.frequency_dict2[num] = self.frequency_dict2.get(num, 0) + 1

    def add(self, index: int, val: int) -> None:
        value = self.nums2[index]
        
        self.frequency_dict2[value] = self.frequency_dict2[value] - 1
        
        self.nums2[index] = self.nums2[index] + val
        value = self.nums2[index]
        
        self.frequency_dict2[value] = self.frequency_dict2.get(value, 0) + 1
        

    def count(self, tot: int) -> int:
        result = 0
        for i in range(len(self.nums1)):
            result = result + self.frequency_dict2.get(tot - self.nums1[i], 0)
        
        return result

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)