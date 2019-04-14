#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (39.82%)
# Total Accepted:    170.2K
# Total Submissions: 423.4K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted linked list: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # more time less space
    # def sortedListToBST(self, head: ListNode) -> TreeNode:
    #     # use slow fast pointers to find the middle
    #     def build(head):
    #         if head:
    #             prev = slow = fast = head
    #             while fast and fast.next:
    #                 prev = slow
    #                 slow = slow.next
    #                 fast = fast.next.next
    #             # print(slow.val, prev.val)
    #             root = TreeNode(slow.val)
    #             if prev != slow:
    #                 prev.next = None
    #                 root.left = build(head)
    #                 root.right = build(slow.next)

    #             return root
    #     return build(head)

    # more space, less time 
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # convert linked list to array
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        
        def build(array):
            if array:
                mid = len(array)//2
                node = TreeNode(array[mid])
                node.left = build(array[:mid])
                node.right = build(array[mid+1:])
                return node
        
        return build(temp)


