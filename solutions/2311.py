"""
    Question 2311: https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

    Very interesting question! Use some DP from right to left, always trying to form the longest substring whose value doesn't exceed k.
    Make a dp array and define dp[start] as "the length of the longest substring which starts at index start in the s string", and then
    the answer comes naturally.
"""


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        N = len(s)
        
        dp = [None for i in range(N)]
        if int(s[-1]) <= k:
            dp[-1] = {
                'value': int(s[-1]),
                'length': 1
            }
        else:
            dp[-1] = {
                'value': 0,
                'length': 0
            }

        for start in range(N - 2, -1, -1):
            best_option = {
                'length': 0,
                'value': 0,
            }

            for index in range(start + 1, N, 1):
                length = dp[index]['length']
                value = dp[index]['value']
                possible_value = int(s[start]) * 2 ** length + value

                if possible_value <= k:
                    if best_option['length'] < dp[index]['length']:
                        best_option = {
                            'length': dp[index]['length'],
                            'value': dp[index]['value']
                        }
                    elif best_option['length'] == dp[index]['length'] and best_option['value'] > dp[index]['value']:
                        best_option['value'] = dp[index]['value']
            
            dp[start] = {
                'length': best_option['length'] + 1,
                'value': int(s[start]) * 2 ** best_option['length'] + best_option['value'] 
            }
        
        return max(map(lambda el: el['length'], dp))
