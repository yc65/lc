#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (41.94%)
# Total Accepted:    264K
# Total Submissions: 626K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
# 
# Example:
# 
# 
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# 
#
class Solution:
    # two pointers
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_left = max_right = 0
        res = 0
        while left < right:
            if height[left] < height[right]:
                if height[left]>=max_left:
                    max_left = height[left]
                else:
                    res += max_left-height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    res += max_right-height[right]
                right -= 1
        return res

