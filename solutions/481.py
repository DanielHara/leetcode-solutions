"""
    Question 481: https://leetcode.com/problems/magical-string/

    This is a very cool question!
    Try to build string s. Using the property described in the problem, use a count_index counter
    to know how many characters you have to append to the string at each step. Use the last character in the string
    to know whether you need to append '1' or '2'.
"""


class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 3:
            return 1

        s_array = ['1', '2', '2']

        count_index = 2
        while len(s_array) < n:
            last_char = s_array[-1]

            if last_char == '1':
                amount = int(s_array[count_index])
                for dummy in range(amount):
                    s_array.append('2')
            else:
                amount = int(s_array[count_index])
                for dummy in range(amount):
                    s_array.append('1')
            
            count_index = count_index + 1
    
        result = 0
        for char_index in range(0, n):
            if s_array[char_index] == '1':
                result = result + 1

        return result
