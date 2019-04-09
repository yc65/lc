#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (49.70%)
# Total Accepted:    362.8K
# Total Submissions: 729.8K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given two binary trees, write a function to check if they are the same or
# not.
# 
# Two binary trees are considered the same if they are structurally identical
# and the nodes have the same value.
# 
# Example 1:
# 
# 
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
# 
# ⁠       [1,2,3],   [1,2,3]
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:     1         1
# ⁠         /           \
# ⁠        2             2
# 
# ⁠       [1,2],     [1,null,2]
# 
# Output: false
# 
# 
# Example 3:
# 
# 
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
# 
# ⁠       [1,2,1],   [1,1,2]
# 
# Output: false
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
    # recursion
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def recur(tree_x, tree_y):
            if not tree_x and not tree_y:
                return True
            if not tree_x or not tree_y:
                return False
            if tree_x.val != tree_y.val:
                return False
            return recur(tree_x.left, tree_y.left) and recur(tree_x.right, tree_y.right)
        res = recur(p, q)
        return res

