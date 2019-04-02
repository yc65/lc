#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (47.26%)
# Total Accepted:    245.4K
# Total Submissions: 516.5K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [3,2,1]
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursive
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     res = []
    #     def dfs_postorder(node):
    #         if node:
    #             dfs_postorder(node.left)
    #             dfs_postorder(node.right)
    #             res.append(node.val)
    #     dfs_postorder(root)
    #     return res
    # iterative
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        stack = []

        while 1:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root.right and stack and stack[-1] == root.right:
                stack.pop()
                stack.append(root)
                root = root.right
            else:
                res.append(root.val)
                root = None
            if not stack:
                break
            
        return res   

