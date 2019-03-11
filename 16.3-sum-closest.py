#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (40.85%)
# Total Accepted:    292.3K
# Total Submissions: 709.6K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        len_nums = len(nums)
        closest = None
        for i in range(len_nums-2):
            j = i+1
            k = len_nums-1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if closest == None:
                    closest = temp
                if abs(temp - target) < abs(closest - target):
                    closest = temp
                if temp < target:
                    j += 1
                elif temp > target:
                    k -= 1
                else:
                    return closest
        return closest

