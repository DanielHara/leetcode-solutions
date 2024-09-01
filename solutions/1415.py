# Question 1415: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

"""
    Just brute-force, as the constraints are low: 1 <= n <= 10, 1 <= k <= 100. Enumerate all happy strings, and return the k-th.
"""

class Solution:
    def generateHappyStrings(self, n: int, start_char: str) -> List[str]:
        if n == 1:
            return [[start_char]]
        
        strings = None

        if start_char == 'a':
            strings = self.generateHappyStrings(n - 1, 'b') + self.generateHappyStrings(n - 1, 'c')
        if start_char == 'b':
            strings = self.generateHappyStrings(n - 1, 'a') + self.generateHappyStrings(n - 1, 'c')
        if start_char == 'c':
            strings = self.generateHappyStrings(n - 1, 'a') + self.generateHappyStrings(n - 1, 'b')

        result = []
        for string in strings:
            string.append(start_char)
            result.append(string)
        
        return result

    def getHappyString(self, n: int, k: int) -> str:
        strings = []

        for char in ['a', 'b', 'c']:
            strings = strings + self.generateHappyStrings(n, char)
        
        happy_strings = []
        for string in strings:
            happy_strings.append(''.join(reversed(string)))

        return happy_strings[k - 1] if len(happy_strings) >= k else ''

