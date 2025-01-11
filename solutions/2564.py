"""
    Question 2564: https://leetcode.com/problems/substring-xor-queries/
    
    You don't want an O(N**2) solution, given the constraints. But the value of first ^ second, given the constraints,
    will be at most 10**9, which fits in 30 bits.
    So, just consider the substrings of s which have at most 30 characters, which is a O(30*N), that is, O(N) solution
"""

class Solution:
    def getBinaryString(self, val: int) -> str:
        if val == 0:
            return '0'

        digits = []
        while val > 0:
            digits.append(str(val % 2))
            val = val // 2

        digits.reverse()
        return ''.join(digits)
    
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        # val = first ^ second, for each query, will fit in 30 bits
        substring_to_indexes_dictionary = {}
        for start_position in range(len(s)):
            substring = ''
            for end_position in range(start_position, min(start_position + 30, len(s))):
                substring = substring + s[end_position]
                if substring not in substring_to_indexes_dictionary:
                    substring_to_indexes_dictionary[substring] = [start_position, end_position]

        result = []
        for [first, second] in queries:
            val = first ^ second
            binary_val = self.getBinaryString(val)

            result.append(substring_to_indexes_dictionary.get(binary_val, [-1, -1]))
            
        return result
