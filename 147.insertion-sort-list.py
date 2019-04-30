#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        p = dummy = ListNode(-1)
        curr = dummy.next = head
        while curr and curr.next:
            # print(curr.val, curr.next.val)
            if curr.val < curr.next.val:
                curr = curr.next
                continue
            p = dummy
            while p.next.val < curr.next.val:
                p = p.next
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = p.next
            p.next = nxt

        return dummy.next


