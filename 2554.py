"""
    Question 2554: https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/
    
    Quite easy question, just do it greedily.
    I don't understand why it's rated as Medium.
"""

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banner_set = set()

        for number in banned:
            banner_set.add(number)
        
        s = 0
        result = 0
        for i in range(1, n + 1):
            if i not in banner_set:
                s = s + i
                
                if s > maxSum:
                    return result
                else:
                    result = result + 1
        return result
