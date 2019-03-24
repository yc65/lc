#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (26.66%)
# Total Accepted:    181.8K
# Total Submissions: 681.3K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, rotate the list to the right by k places, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# 
# 
# Example 2:
# 
# 
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        len_list = 0
        h = head
        while head:
            len_list+=1
            head=head.next
        if len_list == 0: return h
        n = k%len_list
        if n == 0 or len_list == 1: return h
        
        count = 0
        head = h
        new_tail, new_h, tail = None, None, None
        new_h_id = len_list-n
        while head:
            if count == new_h_id - 1:
                new_tail = head
            elif count == new_h_id:
                new_h = head
            if count == len_list-1:
                tail = head
            count += 1
            head = head.next
        # assert tail != None and new_h != None
        new_tail.next = None
        tail.next = h
        return new_h

