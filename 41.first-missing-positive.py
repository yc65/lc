#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (28.24%)
# Total Accepted:    195.7K
# Total Submissions: 690.4K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
# 
# Example 1:
# 
# 
# Input: [1,2,0]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [3,4,-1,1]
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: [7,8,9,11,12]
# Output: 1
# 
# 
# Note:
# 
# Your algorithm should run in O(n) time and uses constant extra space.
# 
#
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # notice: find the first MISSING positive, not to find the smallest positive!
        i, len_nums = 0, len(nums)
        while i < len_nums:
            # notice: use while loop, since after the first swap, the condition could still be unsatisfied on index of i
            # as long as nums[i] is positive, we need to try to put it to nums[nums[i]-1]
            while nums[i] <= len_nums and nums[i] > 0 and nums[nums[i]-1] != nums[i]:
                # notice: use temp to store nums[i]-1
                # if using nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
                # we won't ge the correct result since the nums[i] has been changes in the first assignment
                temp = nums[i]-1
                nums[i], nums[temp] = nums[temp], nums[i]
            i += 1
        for idx, n in enumerate(nums):
            if idx !=n-1:
                return idx+1

        return len_nums+1
