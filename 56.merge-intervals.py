#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (35.03%)
# Total Accepted:    316.5K
# Total Submissions: 903.2K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        intervals.sort(key=lambda x: x.start)
        stack = []
        for i in intervals:
            # print(i.start, i.end)
            if stack:
                top = stack.pop()
                # print("top ",top.start, top.end)
                if i.start >= top.start and i.start <= top.end:
                    if i.end >= top.end:
                        top.end = i.end
                    stack.append(top)
                else:
                    stack.append(top)
                    stack.append(i)
            else:
                stack.append(i)
            # print("stack len:", len(stack) )
        return stack
