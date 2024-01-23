# Question 989: https://leetcode.com/problems/add-to-array-form-of-integer/

"""
    Simply CS 101 (or even secondary school). It reminded me of the carry signal of the digital circuits course
    101 at my dear alma mater ITA (https://en.wikipedia.org/wiki/Instituto_Tecnol%C3%B3gico_de_Aeron%C3%A1utica if you're curious)
"""

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        
        carry = 0
        while (k > 0 or carry > 0) and i >= 0:
            add = k % 10
            
            new_num = (num[i] + add + carry) % 10
            carry = 1 if num[i] + add + carry >= 10 else 0
            
            k = int(k / 10)
            
            num[i] = new_num
            i = i - 1
        
        while k > 0 or carry > 0:
            new_num = (k % 10 + carry) % 10
            num.insert(0, new_num)
            carry = 1 if k % 10 + carry >= 10 else 0
            
            k = int(k / 10)
            
        return num

