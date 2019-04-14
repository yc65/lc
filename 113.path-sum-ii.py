#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (39.69%)
# Total Accepted:    222.7K
# Total Submissions: 555.9K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
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
# ⁠/  \    / \
# 7    2  5   1
# 
# 
# Return:
# 
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
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
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        res = []
        def recur(node, rest, path):
            if not node:
                return
            # NOTE: the ending condition is for the node to be a leaf, 
            # not the Null node. If using the Null node condition, the 
            # path will be added twice - once for the left and once for
            # the right
            if not node.left and not node.right:
                if rest == node.val:
                    res.append(path+[node.val])
                    return True
                else:
                    return False
            l = recur(node.left, rest-node.val, path+[node.val])
            r = recur(node.right, rest-node.val, path+[node.val])
            # if not node.left:
            #     return r
            # if not node.right:
            #     return l
            if l and r:
                return True
            else:
                return False
        recur(root, sum_, [])
        return res

