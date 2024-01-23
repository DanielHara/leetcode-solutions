# Question 2384: https://leetcode.com/problems/largest-palindromic-number/

"""
    Quite easy question
"""

class Solution:
    def largestPalindromic(self, num: str) -> str:
        frequency_dict = {}

        for char in num:
            frequency_dict[char] = frequency_dict.get(char, 0) + 1
        
        frequency_dict_result = {}
        for [char, frequency] in frequency_dict.items():
            frequency_dict_result[char] = frequency // 2
        
        additional = None
        digit = 9
        while digit >= 0:
            if frequency_dict.get(str(digit), 0) % 2 == 1:
                additional = str(digit)
                break
            digit = digit - 1
        
        
        
        result_array = []
        digit = 9
        while digit >= 0:
            number_of_digits = frequency_dict_result.get(str(digit), 0)
            for i in range(number_of_digits):
                if digit > 0 or result_array:
                    result_array.append(str(digit))

            digit = digit - 1

        if additional:
            result_array.append(additional)
        
        N = len(result_array) - 2 if additional else len(result_array) - 1
        for i in range(N, -1, -1):
            result_array.append(result_array[i])
        
        return ''.join(result_array) if result_array else '0'
