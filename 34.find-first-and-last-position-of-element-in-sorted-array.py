#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (32.99%)
# Total Accepted:    273.3K
# Total Submissions: 826.8K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
#
class Solution:
    # use binary search
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        len_nums = len(nums)
        left, right = 0, len_nums-1
        while left <= right: # use <= instead of <!!
            mid = int((left+right)/2)
            if nums[mid] == target:
                sub_right = sub_left = mid
                while sub_right >= 0 and nums[sub_right] == nums[mid]: # don't forget the first condition
                    sub_right -= 1
                idx = sub_right+1
                while sub_left <len_nums and nums[sub_left] == nums[mid]:
                    sub_left += 1
                idy = sub_left - 1
                return [idx, idy]
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return [-1, -1]

# test cases
# [5,7,7,8,8,10]\n8
# [5,7,7,8,8,10]\n6
## pay attention to the following three
# []\n1
# [2,2]\n2
# [1]\n1
