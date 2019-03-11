#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (45.89%)
# Total Accepted:    521.3K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: 
            return None
        elif l2 and not l1:
            return l2
        elif l1 and not l2:
            return l1

        if l2.val<l1.val:
            l1, l2 = l2, l1
        head = l1

        while l1 and l2:
            if l1.next and l2.val <= l1.next.val:
                temp = l2
                l2 = l2.next
                temp.next = l1.next
                l1.next = temp
            elif l1.next and l2.val>l1.next.val:
                l1 = l1.next
            else:
                break
        if not l1.next: # we've run out of l1
            l1.next = l2
        return head
        
            




        
        

