# Question 1299: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

# Trivial question

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = -1

        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = maximum
            maximum = max(temp, maximum)
        
        return arr
