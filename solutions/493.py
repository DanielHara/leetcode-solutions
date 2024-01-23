"""
Question 493: https://leetcode.com/problems/reverse-pairs/

Really tricky question, I've spent some hours to find the solution.
Basically an enhanced merge sort. Do a normal merge sort and take advantage of the fact that you always
get two sorted arrays. Then, before merging them, find the number of inversions in a O(n) operation.
Overall, it still remains O(n * log n) time complexity.

"""

class Solution:
    # Accumulates the number of inversions
    def mergeSort(self, nums: List[int], i: int, j: int):
        if i >= j:
            return 0
        
        metade = int((i + j) / 2)
        
        a = self.mergeSort(nums, i, metade)
        b = self.mergeSort(nums, metade + 1, j)
        
        result = a + b
        
        p = i
        q = metade + 1
        
        temp = []
        while p <= metade and q <= j:
            if nums[p] <= 2 * nums[q]:
                p = p + 1
            else:
                result = result + (metade - p + 1)
                q = q + 1
        
        p = i
        q = metade + 1
        
        temp = []
        while p <= metade and q <= j:
            if nums[p] <= nums[q]:
                temp.append(nums[p])
                p = p + 1
            else:
                temp.append(nums[q])
                q = q + 1
        
        while p <= metade:
            temp.append(nums[p])
            p = p + 1
        
        while q <= j:
            temp.append(nums[q])
            q = q + 1
                
        while temp:
            el = temp.pop(0)
            nums[i] = el
            i = i + 1
    
        return result
    
    def reversePairs(self, nums: List[int]) -> int:
        # Do it using mergeSort:
        
        result = self.mergeSort(nums, 0, len(nums) - 1)
        
        return result
