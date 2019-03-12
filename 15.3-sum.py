#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (23.44%)
# Total Accepted:    492K
# Total Submissions: 2.1M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        runner = 0
        results = []

        while runner < len(nums) and nums[runner] <= 0:
            results += self.twoSum(0 - nums[runner], nums[runner + 1:])
            while runner + 1 < len(nums) and nums[runner + 1] == nums[runner]:
                runner += 1
            runner += 1
        
        return results

    def twoSum(self, target, nums):
        left = 0
        right = len(nums) - 1
        results = []
        while left < right:
            if nums[left] + nums[right] == target:
                results.append([0 - target, nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return results
