#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (32.34%)
# Total Accepted:    172.8K
# Total Submissions: 532.8K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# 
# Example 1:
# 
# 
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# 
# 
# Example 2:
# 
# 
# Input: 1->1->1->2->3
# Output: 2->3
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # my own: three pointers, slow...
    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     if not head or  not head.next: # there's zero or one element
    #         return head
    #     dummy = ListNode(None)
    #     dummy.next = head
    #     h_orig = dummy
    #     prev = dummy
    #     i = head
    #     j = head.next
    #     if i.val == j.val:
    #         dup = True
    #     else:
    #         dup = False
    #     while 1:
    #         if i.val == j.val:
    #             j = j.next
    #             dup = True
    #         elif dup:
    #             prev.next = j
    #             i = j
    #             j = j.next
    #             dup = False
    #         else:
    #             prev = i
    #             i = j
    #             j = j.next
    #             dup = False

    #         if not j:
    #             if dup:
    #                 prev.next = j
    #             break
    #     return h_orig.next
    
    # two pointers:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                # NOTE: the use of while loop within the while loop
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return dummy.next



