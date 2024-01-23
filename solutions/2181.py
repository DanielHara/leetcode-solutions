# Question 2181: https://leetcode.com/problems/merge-nodes-in-between-zeros/

"""
Quite an easy question about list
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        t = head

        while p is not None:
            q = p.next

            s = 0
            while q is not None and q.val != 0:
                s = s + q.val
                q = q.next

            p = q
            t.val = s
            t = t.next
        
        t = head
        while t is not None and t.next is not None and t.next.val != 0:
            t = t.next

        t.next = None

        return head
