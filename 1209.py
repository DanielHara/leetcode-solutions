# Question 1047: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

"""
    Following-up on question, use a stack to do it!
    As has limit 2 <= k <= 10**4, it would be prohibitively expensive to do sequential search when verifying in the same
    if you have reached k sequential equal characters. But what you can do is to store the count of equal consecutive characters,
    and not the sequence of characters themselves.
    This guarantees O(N) time.
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if stack and stack[-1]['char'] == char:
                if stack[-1]['count'] == k - 1:
                    stack.pop()
                else:
                    stack[-1]['count'] = stack[-1]['count'] + 1
            else:
                stack.append({
                    'char': char,
                    'count': 1
                })

        return ''.join([(el['char'] * el['count']) for el in stack])
