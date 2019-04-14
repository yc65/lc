#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (38.25%)
# Total Accepted:    147K
# Total Submissions: 380.6K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# 
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# 
# Return the following binary tree:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    # tree traversal
    # In the inorder list, the list could be partitioned into left tree and right tree
    # by a root node
    # similar to 105
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inord_map = {i:idx for idx, i in enumerate(inorder)}
        def build(left, right):
            if postorder: # don't forget this condition for pop
                curr = postorder.pop()
                idx = inord_map[curr]
                node = TreeNode(curr)
                if idx != right:
                    node.right = build(idx+1, right)
                if idx != left:
                    node.left = build(left, idx-1)
                return node
        return build(0, len(inorder)-1)

