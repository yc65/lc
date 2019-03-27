#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (35.37%)
# Total Accepted:    170.5K
# Total Submissions: 480.4K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
# 
# 
# 
# 
# Example:
# 
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
# Note:
# 
# 
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse_k(self, head, k):
        if not head.next: return head, head, None
        prev = None
        orig_head = curr = head
        count = 0
        if head.next:
            nxt = head.next
        else:
            return head
        # draw on a paper to visualize..
        while curr and count < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1
        if count < k: # it the rest is less than k, reverse the reversed list
            return self.reverse_k(prev, count)
        else:
            # orig_head is the tail, prev is the head, curr is the next after tail
            return orig_head, prev, curr

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1: return head
        s = ListNode(0)
        s.next = head
        prev = s
        while head:
            # reverse k elements
            tail, h, nxt = self.reverse_k(head, k)
            # update as if the reversed k element is a single unit
            prev.next = h
            tail.next= nxt
            prev = tail
            head = nxt

        return s.next

# []\n2
# [0]\n1
# [1]\n1
# [1,2]\n2
# [1,2,3]\n2
# [1,2,3,4]\n3
# [1,2,3,4,5,6]\n3


