#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (39.82%)
# Total Accepted:    212K
# Total Submissions: 526.1K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# 
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # hashmap to speed up
        inorder_map = {i: idx for idx, i in enumerate(inorder)}
        def build(left, right):
            if preorder:
                # pop the first element inthe preorder, this is the root
                curr = preorder.pop(0)
                # find the idx of the root in the inorder list
                idx = inorder_map[curr]
                root = TreeNode(curr)
                # left of the idx is the left subtree
                if idx != left:
                    root.left = build(left, idx-1)
                # right of the idx is the right subtree
                if idx != right:          
                    root.right = build(idx+1, right)
                return root 
        res = build(0, len(inorder))
        return res




