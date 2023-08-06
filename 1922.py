# Question 1922: https://leetcode.com/problems/count-good-numbers/

# Reading https://en.wikipedia.org/wiki/Modular_exponentiation gave me the answer to this question

class Solution:
    def modular_exponentiation(self, exponent: int, base: int) -> int:
        modulus = 10**9 + 7

        result = 1
        base = base % modulus
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            exponent = exponent // 2
            base = (base * base) % modulus

        return result
    
    def countGoodNumbers(self, n: int) -> int:
        odd_indices = n // 2
        even_indices = n - odd_indices
        
        return (self.modular_exponentiation(even_indices, 5) * self.modular_exponentiation(odd_indices, 4)) % (10**9+7)
        