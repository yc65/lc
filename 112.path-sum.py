#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (37.19%)
# Total Accepted:    300.6K
# Total Submissions: 803.1K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
# 
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \      \
# 7    2      1
# 
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum_: int) -> bool:
        if not root and not sum_:return False # 
        def recur(root, rest):
            # print(rest)
            if not root:
                if rest == 0:
                    return True
                else:
                    return False
            res_l = recur(root.left, rest-root.val)
            res_r = recur(root.right, rest-root.val)
            # NOTE: the following two lines
            # we need to compare the l, r, depth only when
            # both these two depth exist
            if not root.left :
                return res_r
            if not root.right:
                return res_l
            if res_l == True or res_r == True:
                return True
            else:
                return False
        return recur(root, sum_)
