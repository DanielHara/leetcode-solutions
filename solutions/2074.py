# Question 2074: https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

"""
  Not a difficult question, just a bit of work with linked lists
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        group_length = 1

        p = head
        ant = head
        while p is not None:
            total = 0
            t = p
            while t is not None and total < group_length:
                total = total + 1
                t = t.next


            count = 0
            if total % 2 == 0:     
                stack = []
                while p is not None and count < group_length:
                    stack.append(p)
                    count = count + 1
                    p = p.next
            
                q = ant
                while stack:
                    q.next = stack.pop()
                    q = q.next
                
                q.next = p
                ant = q


                # list will resume from p
            else:
                while p is not None and count < group_length:
                    ant = p
                    p = p.next
                    count = count + 1
            
            group_length = group_length + 1

        return head
