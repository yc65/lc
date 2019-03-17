#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (27.50%)
# Total Accepted:    157.4K
# Total Submissions: 570K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# Example:
# 
# 
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# ⁠   Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# Note:
# 
# You can assume that you can always reach the last index.
# 
#
class Solution:
    # dp solution TIME EXCEED
    # def jump(self, nums: List[int]) -> int:
    #     len_nums = len(nums)
    #     if len_nums == 1: return 0
    #     cache = [0] * len_nums
    #     for i, n in enumerate(nums):
    #         if i + n >= len_nums-1:
    #             if cache[-1]:
    #                 return min(cache[i] + 1, cache[-1])
    #             else:
    #                 return cache[i]+1
    #         for j in range(i+1, i+n+1):
    #             if cache[j]:
    #                 cache[j] = min(cache[j], cache[i]+1)
    #             else:
    #                 cache[j] = cache[i]+1
    #     return cache[-1]

    # greedy solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        last = 0
        curr = 0
        for i, val in enumerate(nums):
            if i > last:
                last = curr
                steps+=1
            curr = max(curr, i+val)
        return steps

