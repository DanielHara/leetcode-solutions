# Question 2807: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/

"""
    Just do it. As the constraints are quite low (1 <= Node.val <= 1000), even brute-forcing getGreatestCommonDivisor is enough.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getGreatestCommonDivisor(self, num1: int, num2: int) -> int:
        for candidate in range(min(num1, num2), 0, -1):
            if num1 % candidate == 0 and num2 % candidate == 0:
                return candidate

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p is not None and p.next is not None:
            q = p.next
            p.next = ListNode(self.getGreatestCommonDivisor(p.val, q.val))
            p.next.next = q

            p = q

        return head
