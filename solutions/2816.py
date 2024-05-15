"""
    Question 2816: https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

    Not a difficult question
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        p = head
        while p is not None:
            stack.append(p)

            p = p.next
        
        overflow = 0
        while stack:
            p = stack.pop()

            val = (2 * p.val + overflow) % 10
            overflow = (2 * p.val + overflow) // 10

            p.val = val
        
        if overflow == 0:
            return head
        
        new_head = ListNode()
        new_head.val = overflow
        new_head.next = head

        return new_head
