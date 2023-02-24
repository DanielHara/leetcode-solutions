# Question 2165: https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

"""
    Maximize the absolute value of number if it's negative, and minimize it (avoiding leading zero) if the number is positive.
    Quite trivial question.
"""

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if num >= 0:
            frequency_dict = {}
            while num > 0:
                digit = num % 10
                
                frequency_dict[digit] = frequency_dict.get(digit, 0) + 1
                num = num // 10
            
            least_digit = None
            for digit in digits[1:]:
                if digit in frequency_dict:
                    least_digit = digit
                    frequency_dict[digit] = frequency_dict[digit] - 1
                    if frequency_dict[digit] == 0:
                        del frequency_dict[digit]
                    break
            
            stack = [least_digit]

            for digit in digits:
                for i in range(frequency_dict.get(digit, 0)):
                    stack.append(digit)
            
            result = 0
            i = 0
            while stack:
                result = result + stack.pop() * 10 **i
                i = i + 1
            
            return result

        num = (-1)*num
        frequency_dict = {}
        while num > 0:
            digit = num % 10
            
            frequency_dict[digit] = frequency_dict.get(digit, 0) + 1
            num = num // 10
        
        stack = []

        for digit in reversed(digits):
            for i in range(frequency_dict.get(digit, 0)):
                stack.append(digit)
        
        result = 0
        i = 0
        while stack:
            result = result + stack.pop() * 10 ** i
            i = i + 1
        
        return (-1)*result
