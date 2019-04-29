#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return None
        slow, fast = head, head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        
        # reverse head2
        prev, curr = None, head2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        new_head2 = prev
        # print(new_head2.val)
        # merge two heads
        curr = head
        while curr and new_head2:
            head1_next = curr.next
            head2_next = new_head2.next
            curr.next = new_head2
            new_head2.next = head1_next
            curr = head1_next
            new_head2 = head2_next
        

            
