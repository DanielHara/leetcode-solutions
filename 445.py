"""
Question 445: https://leetcode.com/problems/add-two-numbers-ii/

I've used an approach using stacks.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []

        p = l1
        while p is not None:
            stack1.append(p.val)
            p = p.next

        stack2 = []
        q = l2
        while q is not None:
            stack2.append(q.val)
            q = q.next

        stack = []
        carry = 0
        while stack1 or stack2:
            a = stack1.pop() if stack1 else 0
            b = stack2.pop() if stack2 else 0

            stack.append((a + b + carry) % 10)
            carry = 1 if a + b + carry >= 10 else 0

        if carry == 1:
            stack.append(1)

        el = stack.pop()

        answer = ListNode(el)

        p = answer
        while stack:
            el = stack.pop()
            p.next = ListNode(el)
            
            p = p.next

        return answer
