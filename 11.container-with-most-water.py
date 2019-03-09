#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (42.69%)
# Total Accepted:    324.5K
# Total Submissions: 758.2K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
# 
# 
# 
# 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49. 
# 
# 
# 
# Example:
# 
# 
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# 
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0: return 0
        i, j = 0, len(height)-1 # start with the outer most two lines
        res = 0

        while i<j:
            curr = min(height[i], height[j]) * (j-i)
            if curr > res:
                res = curr
             # we only move the shorter line inward. There is a chance to increase the area 
             # when moving the shorter line, since the capacity is constrained by the shorter one
            if height[i]>height[j]:
                j -= 1
            else:
                i += 1
        return res

# test cases:
# [1,2,3,4,5,6,7]
# []
# [3,7,2,5,3,7,5]
