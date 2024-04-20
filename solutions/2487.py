"""
    Question 2487: https://leetcode.com/problems/remove-nodes-from-linked-list/

    Just use a stack.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        ids_to_remove = set()

        p = head
        while p is not None:
            while stack and stack[-1][1] < p.val:
                element = stack.pop()
                ids_to_remove.add(element[0])

            stack.append([id(p), p.val])

            p = p.next

        new_head = head
        while new_head and id(new_head) in ids_to_remove:
            new_head = new_head.next
        
        if new_head is None:
            return None
        
        p = new_head
        while p:
            if p.next and id(p.next) in ids_to_remove:
                p.next = p.next.next
            else:
                p = p.next

        return new_head
        

        