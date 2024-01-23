"""
Question 2130: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

I just adapted my answer to question 234 (see 234.py) for a O(n) time and O(1) space solution.
The only difference is that, instead of comparing the two linked lists, we take the maximum of the sum of the values
pointed by each of the two pointers.

This solution is O(n) time and O(1) space, and was faster than 95.09% of submitted solutions in time and used less memory 
than 96.71% of submitted solutions.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        p = head
        
        length = self.findLength(head)
        if length == 1:
            return True
        
        i = 1 
        while i < int(length / 2):
            p = p.next
            i = i + 1
        
        if length % 2 == 1:    
            q = p.next.next
            
            p.next = None
        else:
            q = p.next
            p.next = None
        
    
        p = self.reverseList(head)
        
        # Compare p and q
        
        result = 0
        while p and q:
            result = max(result, p.val + q.val)
            p = p.next
            q = q.next
        
        return result
    
    
    def findLength(self, head: Optional[ListNode]) -> int:
        result = 0
        
        while head is not None:
            result = result + 1
            head = head.next
        
        return result

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        
        ant = None
        while p is not None:
            q = p.next
            p.next = ant
            ant = p
            p = q
        
        return ant
        
