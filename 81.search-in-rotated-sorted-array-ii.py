#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (32.49%)
# Total Accepted:    162.1K
# Total Submissions: 498.8K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
# 
# You are given a target value to search. If found in the array return true,
# otherwise return false.
# 
# Example 1:
# 
# 
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# 
# Follow up:
# 
# 
# This is a follow up problem to Search in Rotated Sorted Array, where nums may
# contain duplicates.
# Would this affect the run-time complexity? How and why?
# 
# 
#
class Solution:
    # NOTE: compare with serach in rotated sorted array i
    # binary search
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        left, right = 0, len(nums)-1
        while left <= right: # notice the <= not < 
            # print(left, right)
            # if we have 3333123, mid == left = right, we no longer could
            # judge which part the target is in. The following two lines
            # serves to find the mid
            # c.f. compare with serach in rotated sorted array i
            while left < right and nums[left] == nums[right]:
                left += 1
            mid = (left+right+1)//2
            if target == nums[left] or target == nums[right] or target == nums[mid]:
                return True
            elif target > nums[left] and target < nums[mid]:
                right = mid-1
            elif target > nums[mid] and target < nums[right]:
                left = mid+1
            elif nums[left] > nums[mid]:
                right = mid - 1
            elif nums[right] < nums[mid]:
                left = mid + 1
            else: # don's forget this! if not found, the while loop does not stop triggered by 
                  # left > right, since left and right are updated according to mid.
                return False
        # return False

