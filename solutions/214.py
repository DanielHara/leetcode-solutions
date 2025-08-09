"""
    Question 214: https://leetcode.com/problems/shortest-palindrome/

    Use a rolling hash to do it!
    Iterate through the string, and at each pass, calculate hash(s[0: end]), and hash(reversed(s[0: end]))
    If both hashes are equal, you have a palindrome. Get the largest value for end for which s[0:end] is a palindrome.
    Then, get the rest of the string, s[end:], reverse it and add it to the beginning of the original string.
"""

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rolling_hash = 0
        inverted_rolling_hash = 0

        k = ord('z') - ord('a') + 1

        max_length = 0

        power = 1
        for index, char in enumerate(s):
            char_hash = ord(char) - ord('a')
            rolling_hash = k * rolling_hash + char_hash
            inverted_rolling_hash = inverted_rolling_hash + char_hash * power
            power = power * k

            if rolling_hash == inverted_rolling_hash:
                max_length = index

        # s[0:max_length + 1] is a palindrome
        prefix = ''.join(reversed(s[max_length + 1:]))

        return prefix + s
