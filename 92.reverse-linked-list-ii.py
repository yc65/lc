#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (34.22%)
# Total Accepted:    184.5K
# Total Submissions: 537K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        i, j = None, head
        while m>1:
            i = j
            j = j.next
            m, n = m-1, n-1
        connect, tail = i, j

        while n:
            temp = j.next
            j.next = i
            # print (j.val, '->',j.next.val)
            i = j
            j = temp                
            n-=1
        
        if connect:
            connect.next = i
        else:
            head = i
        tail.next = j
        
        return head
