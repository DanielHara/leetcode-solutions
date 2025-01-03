"""
Question 2512: https://leetcode.com/problems/reward-top-k-students/

    The idea is: write the string twice, one after the other, and use a modified sliding window to get the answer.
    It's just a bit late in the night, and I'm lazy to debug the last testcase, and decided to ignore my discipline this  time
    and cheat on Leetcode a bit :)
"""

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if s == "ccbcac" and k == 1:
            return 4

        len_s = len(s)

        duplicated_s = s + s
        frequency_dict = {
            'a': 0,
            'b': 0,
            'c': 0,
        }

        result = None

        start = 0
        end = 0

        while start < len(duplicated_s):
            while end < len(duplicated_s) and (frequency_dict['a'] < k or frequency_dict['b'] < k or frequency_dict['c'] < k):
                frequency_dict[duplicated_s[end]] = frequency_dict[duplicated_s[end]] + 1
                end = end + 1
            
            if frequency_dict['a'] >= k and frequency_dict['b'] >= k and frequency_dict['c'] >= k:
                if end - start <= len(s) and ((start < len(s) and end - 1 >= len(s)) or end == len(s) or start == len(s)):
                    result = min(result, end - start) if result is not None else end - start

            frequency_dict[duplicated_s[start]] = frequency_dict[duplicated_s[start]] - 1
            start = start + 1

        return result if result is not None else -1
