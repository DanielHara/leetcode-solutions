"""
Question 876: https://leetcode.com/problems/middle-of-the-linked-list/

A fairly easy question. We just can't get around with going through the whole list to work out its length.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findLength(self, head: Optional[ListNode]) -> int:
        result = 0
        
        while head is not None:
            result = result + 1
            head = head.next
        
        return result

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.findLength(head)
        
        i = 0
        p = head
        while i < int(length / 2):
            p = p.next
            i = i + 1
        
        return p    
