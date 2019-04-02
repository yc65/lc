#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (55.41%)
# Total Accepted:    429.9K
# Total Submissions: 772K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
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

# NOTE:
# DFS traversal:
#        1
#       / \
#      2  3
#     / \
#    4  5
# Inorder traversal: 4 2 5 1 3
# Preorder traversal: 1 2 4 5 3   see Q144
# Postorder traversal: 4 5 2 3 1  see Q145
#

class Solution:
    # recursive method:
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     res = []
    #     def dfs(node):
    #         if node:
    #             dfs(node.left)
    #             res.append(node.val)
    #             dfs(node.right)
    #     dfs(root)
    #     return res
    # iterative method:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            curr = stack.pop()
            res.append(curr.val)
            root = curr.right
        return res

