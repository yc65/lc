#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (25.47%)
# Total Accepted:    380.4K
# Total Submissions: 1.5M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# Example 1:
# 
# 
# Input:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# Output: true
# 
# 
# Example 2:
# 
# 
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# Output: false
# Explanation: The input is: [5,1,4,null,null,3,6]. The root node's
# value
# is 5 but its right child's value is 4.
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
    # piggyback on the inorder traversal
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        inorder = float('-inf') # negative infinite
        while True:
            while root:
                stack.append(root)
                # NOTE: all childrens under the left child should have smaller value 
                # than the root value. Thus don't use the following two lines
                # if root.left and root.val <= root.left.val:
                #     return False
                root = root.left
            if not stack:
                return True
            curr = stack.pop()
            # NOTE: all chidrens under the right child should have bigger value
            # that the root value, thus using the inorder >= curr.val, instead of
            # of the follwing two lines
            # NOTE: if left.val or right.val is the same as root.val, it's not
            # valid either
            # if curr.right and curr.val >= curr.right.val:
            #     return False
            if inorder >= curr.val:
                return False
            inorder = curr.val
            root = curr.right
        return True
            

