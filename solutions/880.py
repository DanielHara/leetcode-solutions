"""
Question 880: https://leetcode.com/problems/decoded-string-at-index/

    A very interesting question! I just used a stack and a bit of math.
"""

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        k = k - 1 # Use 0-indexed

        if not s[-1].isdigit():
            s = s + '1'
        
        tokens = []
        i = 0
        while i < len(s):
            start_i = i
            
            while i < len(s) and not s[i].isdigit():
                i = i + 1

            tokens.append(s[start_i:i])

            times_repeat = 1
            j = i
            while j < len(s) and s[j].isdigit():
                times_repeat = times_repeat * int(s[j])
                j = j + 1
            
            tokens.append(times_repeat)
            i = j
        
        stack = []

        for i in range(0, len(tokens), 2):
            stack.append({
                'length_repeated_string': len(tokens[i]) + (stack[-1]['number_of_repetitions'] * stack[-1]['length_repeated_string'] if stack else 0),
                'number_of_repetitions': tokens[i + 1],
                'appended_string': tokens[i]
            })

        while stack:
            block = stack.pop()
            k = k % block['length_repeated_string']

            if k >= block['length_repeated_string'] - len(block['appended_string']):
                return block['appended_string'][len(block['appended_string']) + k - block['length_repeated_string']]
