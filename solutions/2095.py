"""
Question 2095: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

Easy question after having solved questions 876 and 2130.
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

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        
        length = self.findLength(head)
        
        i = 0
        p = head
        while i < int(length / 2) - 1:
            p = p.next
            i = i + 1
        
        p.next = p.next.next
        
        return head
