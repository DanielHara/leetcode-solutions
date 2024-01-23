"""
Question 234: https://leetcode.com/problems/palindrome-linked-list/

I went straight for trying for a solution in O(n) time and O(1) space.
Go a first time through the list just to find out its length.
Then go to the middle of the list, ignore the middle element, if the length is odd.
Reverse the first half of the list (which can be done in linear time and constant space), and finally
compare the reversed half with the second half. Return True if the values are the same, and False otherwise.

This solution is O(n) time and O(1) space, and was faster than 93.81% of submitted solutions in time and 95.58% in memory usage.
"""

class Solution:
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
            
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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
        
        while p and q:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        
        return True
