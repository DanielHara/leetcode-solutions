# Question 476: https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        binaries = []
        
        while num > 0:
            binaries.append(num % 2)
            num = num // 2
        
        answer = 0
        for index, element in enumerate(binaries):
            if element == 0:
                answer = answer + 2 ** index
        
        return answer
