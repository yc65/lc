#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (33.68%)
# Total Accepted:    176.6K
# Total Submissions: 520K
# Testcase Example:  '{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}'
#
# Given a binary tree
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
# {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
# 
# Output:
# {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}
# 
# Explanation: Given the above binary tree (Figure A), your function should
# populate each next pointer to point to its next right node, just like in
# Figure B.
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
    # def connect(self, root: 'Node') -> 'Node':
    #     if not root: return root
    #     q = [(root, 0)]
    #     while q:
    #         curr_node, level = q.pop(0)
    #         if curr_node.left:
    #             q.append((curr_node.left, level+1))
    #         if curr_node.right:
    #             q.append((curr_node.right, level+1))
    #         if not q or level != q[0][1]:
    #             curr_node.next = None
    #         else:
    #             curr_node.next = q[0][0]
    #     return root

    # O(1) space
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

