#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (59.26%)
# Total Accepted:    444.7K
# Total Submissions: 745.1K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,1]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,1,2,1,2]
# Output: 4
# 
# 
#
class Solution:
    # bit operation
    # a XOR 0 = a
    # a XOR a = 0
    # a XOR b XOR a = a XOR a XOR b = b
    def singleNumber(self, nums: List[int]) -> int:
        if not nums: return None
        a = 0
        for x in nums:
            a ^= x 
        return a

