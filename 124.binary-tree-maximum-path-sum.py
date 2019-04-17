#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (29.68%)
# Total Accepted:    182.5K
# Total Submissions: 614.6K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# Output: 42
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
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        def recur(node):
            if not node:
                return 0
            l = recur(node.left)
            r = recur(node.right)
            curr_max = max([l+node.val, r+node.val, node.val])
            # NOTE: dont use the following one, since when both left and 
            # right of the root are included in the path, the root should
            # not have any ancestors
            # curr_max = max([l+node.val, r+node.val, node.val, l+r+node.val])
            self.res = max(self.res, curr_max, l+r+node.val)
            return curr_max
        recur(root)
        return self.res
