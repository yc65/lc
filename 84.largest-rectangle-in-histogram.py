#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (30.43%)
# Total Accepted:    163.6K
# Total Submissions: 535.8K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
# 
# 
# 
# 
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
# 
# 
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
# 
# 
# 
# Example:
# 
# 
# Input: [2,1,5,6,2,3]
# Output: 10
# 
# 
#
class Solution:
    # stack
    def largestRectangleArea(self, heights: List[int]) -> int:
    # def largestRectangleArea(self, heights):
        stack = [] # the stack stores the IDX of elements in histgram
        len_heights = len(heights)
        idx = 0
        max_area = 0
        while idx < len_heights:
            if (not stack) or (heights[stack[-1]]<=heights[idx]):
                stack.append(idx)
                idx += 1
            else:
                top = stack.pop()
                # the smallest one is always at the bottom, 
                # when the stack is empty, it means the poped one is the smallest
                # the length should be length of all elements before idx
                area = heights[top] * ((idx - stack[-1] -1) if stack else idx)
                max_area = max(max_area, area)
        while stack:
            top = stack.pop()
            area = heights[top] * ((idx - stack[-1] -1) if stack else idx)
            max_area = max(max_area, area)
        # print(max_area)
        return max_area

# if __name__ == "__main__":
#     s = Solution()
#     s.largestRectangleArea([4,3,5,6,2,3])



    