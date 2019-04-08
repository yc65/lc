#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (35.17%)
# Total Accepted:    132.7K
# Total Submissions: 377.3K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
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
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n: return []
        def recur(begin, end):
            res = []
            if begin > end:
                res.append(None)
                return res
            for i in range(begin, end+1):
                left_subtrees = recur(begin, i-1)
                right_subtrees = recur(i+1, end)
                len_left_subtrees = len(left_subtrees)
                len_right_subtrees = len(right_subtrees)
                for m in range(len_left_subtrees):
                    l_sub = left_subtrees[m]
                    for n in range(len_right_subtrees):
                        r_sub = right_subtrees[n]
                        curr_node = TreeNode(i)
                        curr_node.left = l_sub
                        curr_node.right = r_sub
                        res.append(curr_node)
            return res
        out = recur(1, n)
        return out

