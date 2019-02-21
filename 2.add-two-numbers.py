#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (30.51%)
# Total Accepted:    758.3K
# Total Submissions: 2.5M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        add_one = False
        l_root = l1
        while l1 and l2:
            l1.val += l2.val
            if add_one:
                l1.val += 1
            if l1.val>9:
                l1.val-=10
                add_one = True
            else:
                add_one = False
            if l1.next == None or l2.next == None:
                break
            l1=l1.next
            l2=l2.next
        if l1.next:
            l1 = l1.next
            while l1:
                if add_one:
                    l1.val+=1
                if l1.val>9:
                    l1.val-=10
                    add_one = True
                else:
                    add_one = False
                if l1.next == None:
                    break        
                l1 = l1.next
        if l2.next:
            l2 = l2.next
            l1.next = ListNode(0)
            l1 = l1.next
            while l2:
                l1.val += l2.val
                if add_one:
                    l1.val+=1
                if l1.val>9:
                    print("test")
                    l1.val-=10
                    add_one = True
                else:
                    add_one = False
                l2 = l2.next
                if l2 == None:
                    break 
                l1.next = ListNode(0)
                l1 = l1.next
        if add_one:
            l1.next = ListNode(1)
        return l_root


