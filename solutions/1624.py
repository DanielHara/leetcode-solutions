"""
    Question 1624: https://leetcode.com/problems/largest-substring-between-two-equal-characters

    Quite trivial question, no secret on how to solve it
"""

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_to_indexes_map = {}

        for index, char in enumerate(s):
            if char not in char_to_indexes_map:
                char_to_indexes_map[char] = [index]
            else:
                if len(char_to_indexes_map[char]) == 2:
                    char_to_indexes_map[char].pop()
                char_to_indexes_map[char].append(index)
        
        result = -1
        for array in char_to_indexes_map.values():
            if len(array) == 2:
                result = max(result, array[1] - array[0] - 1)

        return result
