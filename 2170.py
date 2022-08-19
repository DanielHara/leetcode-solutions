# Question 2170: https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        result = 0

        frequency_dict = {}
        for i in range(0, len(nums), 2):
            frequency_dict[nums[i]] = frequency_dict.get(nums[i], 0) + 1
        
        array1 = []
        for [key, value] in frequency_dict.items():
            array1.append((value, key))
        
        # Sort by value
        array1.sort(key=lambda x: x[0], reverse=True)
        
        
        frequency_dict = {}
        for i in range(1, len(nums), 2):
            frequency_dict[nums[i]] = frequency_dict.get(nums[i], 0) + 1
        
        array2 = []
        for [key, value] in frequency_dict.items():
            array2.append((value, key))
        
        array2.sort(key=lambda x: x[0], reverse=True)
        
        
        
        if array1 and array2 and array1[0][1] == array2[0][1]:
            if len(array1) == 1 and len(array2) == 1:
                return len(nums) // 2
            
            # First possibility: use the the first element in array1:
            i = 0
            p = 0
            while i < len(array2):
                if array2[i][1] != array1[0][1]:
                    break
                else:
                    p = p + array2[i][0]
                    i = i + 1
            
            i = i + 1
            
            while i < len(array2):
                p = p + array2[i][0]
                i = i + 1
            
            for i in range(1, len(array1)):
                p = p + array1[i][0]
            
            
            result = p
            
            # Second possibility: use the the first element in array2:
            i = 0
            p = 0
            while i < len(array1):
                if array1[i][1] != array2[0][1]:
                    break
                else:
                    p = p + array1[i][0]
                    i = i + 1
            
            i = i + 1
            
            while i < len(array1):
                p = p + array1[i][0]
                i = i + 1
            
            for i in range(1, len(array2)):
                p = p + array2[i][0]
            
            result = min(result, p)
            
            return result
        
        
        result = 0
            
        for i in range(1, len(array1)):
            result = result + array1[i][0]
        
        for i in range(1, len(array2)):
            result = result + array2[i][0]
        
        return result
