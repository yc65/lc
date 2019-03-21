#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (43.00%)
# Total Accepted:    481.4K
# Total Submissions: 1.1M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        len_nums = len(nums)
        dp = [0] * len_nums
        res = dp[0] = nums[0]
        for i in range(1,len_nums):
            if dp[i-1]<0:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i-1]
            if dp[i] > res:
                res = dp[i]
        return res

