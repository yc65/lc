#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (41.36%)
# Total Accepted:    229.1K
# Total Submissions: 548.5K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example, given the following tree:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 
# The flattened tree should look like:
# 
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def recur(node):
            if not node:
                return

            if not node.left and not node.right:
                return node, node
            if not node.left:
                r_head, r_tail = recur(node.right)
                node.right = r_head
                return node, r_tail
            if not node.right:
                l_head, l_tail = recur(node.left)
                node.right = l_head
                node.left = None
                return node, l_tail
            r_head, r_tail = recur(node.right)
            l_head, l_tail = recur(node.left)
            node.right = l_head
            l_tail.right = r_head
            node.left = None
            return node, r_tail
        recur(root)



