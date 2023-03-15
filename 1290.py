# Question 1290: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Quite a trivial question

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        N = 0

        p = head
        while p:
            N = N + 1
            p = p.next
        
        result = 0
        
        p = head
        i = 0
        while p:
            result = result + p.val * 2 ** (N - 1 - i)
            i = i + 1
            p = p.next

        return result
