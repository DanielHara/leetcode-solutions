"""
Question 237: https://leetcode.com/problems/delete-node-in-a-linked-list/

    Very frustrating and poorly described question. It expects you to change the value of the nodes, which
    can be counter-intuitive. I thought I had to really remove the node, that is, really removing the node with id(node).
    However, it's not possible to do that when the node you want to remove is the first one in the list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        node.val = node.next.val
        node.next = node.next.next
