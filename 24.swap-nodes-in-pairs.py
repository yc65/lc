#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (43.22%)
# Total Accepted:    286K
# Total Submissions: 659.6K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # recursive method
        if head and head.next:
            head_next = head.next
            head.next, head_next.next = self.swapPairs(head_next.next), head
            return head_next
        else:
            return head

        # non-recursive methos
        # if not head: return None

        # if head.next == None: return head
        
        # dummy = ListNode(1)
        # dummy.next = head

        # point_prev, point_curr, point_next = dummy, head, head.next

        # while point_curr and point_next:
        #     # swaping
        #     point_curr.next = point_next.next
        #     point_prev.next = point_next
        #     point_next.next=  point_curr

        #     # updating
        #     point_prev = point_curr
        #     if point_curr.next:
        #         point_curr = point_curr.next
        #     else:
        #         break
        #     if point_curr.next:
        #         point_next = point_curr.next
        #     else:
        #         break
        
        # return dummy.next



