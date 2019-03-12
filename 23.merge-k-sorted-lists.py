#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (33.01%)
# Total Accepted:    348.3K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        head = point = ListNode(0) # note: assign the same value to two variables
        # note: index of the list has to be stored. otherwise heapify won't work. why?
        # guess It will compare the node only if the i are equal. and comparing node is not supported
        q = [(node.val, i, node) for i, node in enumerate(lists) if node]

        heapq.heapify(q)
        # for l in lists:
        #     if l:
        #         heapq.heappush(q,(l.val, l))
        while q:
            # q.sort(key=lambda x: x[0], reverse = True)
            # val, node = q.pop()
            val, _,node = heapq.heappop(q)
            point.next = node
            point = point.next
            node = node.next
            if node:
                heapq.heappush(q, (node.val,_, node))
        return head.next


