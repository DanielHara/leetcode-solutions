# Question 1318: https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

"""
    Quite easy question, but interesting anyway.
    Just build the binary representation of all the numbers, and go through it.
"""

class Solution:
    # Suppose all numbers fit into a 32 digit integer
    def getBinaryDigits(self, num: int) -> List[int]:
        digits = []
        
        count = 0
        while count < 32:
            digit = num % 2
            digits.append(digit)
            
            num = num // 2
            count = count + 1
        
        return digits
    
    def minFlips(self, a: int, b: int, c: int) -> int:
        digits_a = self.getBinaryDigits(a)
        digits_b = self.getBinaryDigits(b)
        digits_c = self.getBinaryDigits(c)

        result = 0
        for index in range(32):
            digit_a = digits_a[index]
            digit_b = digits_b[index]
            digit_c = digits_c[index]

            if digit_a | digit_b != digit_c:
                if digit_c == 1:
                    result = result + 1
                else:
                    if digit_a == 1 and digit_b == 1:
                        result = result + 2
                    else:
                        result = result + 1
        
        return result
