#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
#
# algorithms
# Medium (37.00%)
# Total Accepted:    236.1K
# Total Submissions: 632.3K
# Testcase Example:  '{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}'
#
# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children. The binary tree has the following
# definition:
# 
# 
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
# 
# 
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# 
# 
# Example:
# 
# 
# 
# 
# Input:
# {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
# 
# Output:
# {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}
# 
# Explanation: Given the above perfect binary tree (Figure A), your function
# should populate each next pointer to point to its next right node, just like
# in Figure B.
# 
# 
# 
# 
# Note:
# 
# 
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra
# space for this problem.
# 
# 
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    # tree traversal with queue
    # def connect(self, root: 'Node') -> 'Node':
    #     if not root: return root
    #     q = [(root,0)]
    #     while q:
    #         curr_node, curr_level = q.pop(0)
    #         if curr_node.left:
    #             q.append((curr_node.left, curr_level+1))
    #         if curr_node.right:
    #             q.append((curr_node.right, curr_level+1))
    #         # if the poped element is not at the same level 
    #         # as the first element in the queue, then it should
    #         # point to null
    #         # else, it should point to the first element int the queue
    #         if not q or q[0][1] != curr_level:
    #             curr_node.next = None
    #         else:
    #             curr_node.next = q[0][0]
    #     return root

    # O(1) constant
    def connect(self, node: 'Node') -> 'Node':
        head = node
        tail = dummy = Node(0, None, None, None) # tail is the start of the child layer
        while node:
            for c in (node.left, node.right):
                tail.next = c
                if tail.next:
                    tail = tail.next
            node = node.next
            if not node:
                tail = dummy
                node = dummy.next

        return head
