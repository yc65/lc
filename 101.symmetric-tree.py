#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (42.88%)
# Total Accepted:    381.2K
# Total Submissions: 884.5K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# But the following [1,2,2,null,3,null,3]  is not:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursive method
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     def recur(x, y):
    #         if x == None and y == None: return True
    #         if x == None or y == None:return False
    #         if x.val == y.val:
    #             return recur(x.left, y.right) and recur(x.right, y.left)
    #         else:
    #             return False
    #     return recur(root, root)

    # iterative method
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        queue = [root.left, root.right]
        while queue:
            x = queue.pop(0)
            y = queue.pop(0)
            if not x and not y: continue 
            # NOTE: unlike recursive method, don't return anything
            if not x or not y: return False
            if x.val != y.val: return False
            queue.extend([x.left, y.right, x.right, y.left])
        return True



