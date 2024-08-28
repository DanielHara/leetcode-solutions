# Question 1234: https://leetcode.com/problems/replace-the-substring-for-balanced-string/

"""
    Very interesting question!
    The trick is to know the excess of each character, and find the shortest substring which has at least the same number of
    excess characters for each of 'Q', 'W', 'E', and 'R'.
    You can use a sliding window to do that in linear time.
"""

class Solution:
    def balancedString(self, s: str) -> int:
        frequency_dict = {}

        for char in s:
            frequency_dict[char] = frequency_dict.get(char, 0) + 1
        
        excess_dict = {}
        for char, frequency in frequency_dict.items():
            if frequency > len(s) / 4:
                excess_dict[char] = frequency - len(s) / 4

        if not excess_dict:
            return 0
        
        result = None

        frequency_dict = {}
        # Sliding window:
        start = 0
        end = 0
        while start < len(s):
            while end < len(s):
                enough = frequency_dict.get('W', 0) >= excess_dict.get('W', 0) and frequency_dict.get('Q', 0) >= excess_dict.get('Q', 0) and frequency_dict.get('E', 0) >= excess_dict.get('E', 0) and frequency_dict.get('R', 0) >= excess_dict.get('R', 0)
                if enough:
                    result = min(result, end - start) if result is not None else end - start
                    break
                else:
                    frequency_dict[s[end]] = frequency_dict.get(s[end], 0) + 1
                    end = end + 1

            frequency_dict[s[start]] = frequency_dict[s[start]] - 1
            start = start + 1
            
            enough = frequency_dict.get('W', 0) >= excess_dict.get('W', 0) and frequency_dict.get('Q', 0) >= excess_dict.get('Q', 0) and frequency_dict.get('E', 0) >= excess_dict.get('E', 0) and frequency_dict.get('R', 0) >= excess_dict.get('R', 0)
            if enough:
                result = min(result, end - start) if result is not None else end - start
        
        return result
