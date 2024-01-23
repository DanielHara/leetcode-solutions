"""
    Question 2429: https://leetcode.com/problems/minimize-xor/

    Very interesting question! Do it greedily.
"""

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        number_of_set_bits = 0

        while num2 > 0:
            if num2 % 2 == 1:
                number_of_set_bits = number_of_set_bits + 1

            num2 = num2 // 2
        
        set_bit_powers = []
        power = 0
        while num1 > 0:
            if num1 % 2 == 1:
                set_bit_powers.append(power)

            num1 = num1 // 2
            power = power + 1
        
                
        result = 0
        powers_in_result = set()
        while number_of_set_bits > 0 and set_bit_powers:
            power = set_bit_powers.pop()

            result = result + 2 ** power
            powers_in_result.add(power)
            number_of_set_bits = number_of_set_bits - 1
        
        power = 0
        while number_of_set_bits > 0:
            if power not in powers_in_result:    
                result = result + 2 ** power
                number_of_set_bits = number_of_set_bits - 1

            power = power + 1
        
        return result
