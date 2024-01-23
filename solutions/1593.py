# Question 1593: https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings

"""
    Because 1 <= s.length <= 16, you can just brute-force it. Just do it.
    This solution beats 100% (!) of Python solutions in processing time.
"""

class Solution:
    def recursiveMaxUniqueSplit(self, s: str, N: int, previous_set: Set[str]) -> bool:
        if N == 1:
            return s not in previous_set

        if N == 0:
            return len(s) == 0

        previous_set = previous_set.copy()
        for i in range(1, len(s) - N + 2, 1):
            if s[:i] in previous_set:
                continue

            previous_set.add(s[:i])

            possible = self.recursiveMaxUniqueSplit(s[i:], N - 1, previous_set)

            if possible:
                return True

            previous_set.remove(s[:i])
        
        return False


    def maxUniqueSplit(self, s: str) -> int:
        MAX_LENGTH = 16
        
        for count in range(MAX_LENGTH, 0, -1):
            new_set = set()
            if self.recursiveMaxUniqueSplit(s, count, new_set):
                return count
        
        return 1
