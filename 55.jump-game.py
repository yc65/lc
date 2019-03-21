#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (31.45%)
# Total Accepted:    242.7K
# Total Submissions: 771.7K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Determine if you are able to reach the last index.
# 
# Example 1:
# 
# 
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
#
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return True
        len_nums = len(nums)
        curr = 0
        furthest = nums[0]
        while furthest <= len_nums-1:
            if furthest == len_nums-1:return True
            progress = False
            i = curr
            while i <= furthest:
                temp = i+nums[i]
                if temp > furthest:
                    furthest = temp
                    if furthest >= len_nums-1: return True
                    progress = True
                i += 1
            if progress == False:
                return False
            curr = furthest
        return True

