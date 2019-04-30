#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # sort (merge sort of linked list)
    def sortList(self, head: ListNode) -> ListNode:
        return self.sort(head)

    def sort(self, head):
        if not head or not head.next: return head
        # NOTE: how slow and fast pointers are initialized
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        # print (head.val, head.next.val)
        l = self.sort(head)
        r = self.sort(head2)
        return self.merge(l, r)

    def merge(self, l, r):
        # print(l.val, r.val)
        if not l or not r: return l or r
        if l.val > r.val:
            l, r = r, l
        h = l
        while l and r:
            while l.next and l.next.val < r.val:
                l = l.next
            r_n = r.next
            r.next = l.next
            l.next = r
            r = r_n
        if r:
            l.next = r
        return h

