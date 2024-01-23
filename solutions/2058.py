# Question 2058: https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

"""
    This question has no secret either, just do it
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head.next is None:
            return [-1, -1]
        
        # Find critical points:
        critical_points = []

        ant = head
        p = head.next

        count = 1
        while p.next is not None:
            if (ant.val > p.val and p.val < p.next.val) or (ant.val < p.val and p.val > p.next.val):
                critical_points.append(count)
            
            ant = p
            p = p.next
            count = count + 1
        
        if len(critical_points) < 2:
            return [-1, -1]
        
        minimum = critical_points[-1] - critical_points[0]
        for i in range(len(critical_points) - 1):
            minimum = min(minimum, critical_points[i + 1] - critical_points[i])
        
        return [minimum, critical_points[-1] - critical_points[0]]
