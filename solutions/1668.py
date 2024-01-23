"""
Question 1668: https://leetcode.com/problems/maximum-repeating-substring/description/

Looking at the constraints:

1 <= sequence.length <= 100
1 <= word.length <= 100

, I noticed that simple brute-force would do.

"""

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        result = 0

        for i in range(0, len(sequence) - len(word) + 1):
            j = i

            while j < len(sequence) and sequence[j] == word[(j - i) % len(word)]:
                j = j + 1

            result = max(result, (j - i) // len(word))

        return result
