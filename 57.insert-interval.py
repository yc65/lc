#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Hard (30.86%)
# Total Accepted:    167.8K
# Total Submissions: 543.2K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their
# start times.
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# 
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        if not intervals: return [newInterval]
        len_intervals = len(intervals)
        if newInterval.end < intervals[0].start:
            intervals = [newInterval] + intervals
            return intervals
        elif newInterval.start > intervals[-1].end:
            intervals = intervals + [newInterval]
            return intervals
        elif newInterval.start <= intervals[0].start and newInterval.end >= intervals[-1].end:
            return [newInterval]

        overlap_idx = []
        len_intervals = len(intervals)
        n = 0
        while n < len_intervals:

            if intervals[n].start <= newInterval.start and intervals[n].end >= newInterval.start:
                overlap_idx.append(n)
            elif intervals[n].end >= newInterval.end and intervals[n].start <= newInterval.end:
                overlap_idx.append(n)
            elif intervals[n].start > newInterval.start and intervals[n].end < newInterval.end:
                overlap_idx.append(n)
            elif n < len_intervals-1 and intervals[n].end < newInterval.start and intervals[n+1].start > newInterval.end:
                return intervals[:n+1] + [newInterval] + intervals[n+1:]
            n+=1

        intervals[overlap_idx[0]].start = min(newInterval.start, intervals[overlap_idx[0]].start)
        intervals[overlap_idx[0]].end = max(newInterval.end, intervals[overlap_idx[-1]].end)
        if overlap_idx[-1] == len_intervals-1:
            return intervals[:overlap_idx[0]+1]
        else:
            return intervals[:overlap_idx[0]+1] + intervals[overlap_idx[-1]+1:]
        



        # else:
        #     if len_intervals == 1:
        #         intervals[0].start = min(intervals[0].start, newInterval.start)
        #         intervals[0].end = max(intervals[0].end, newInterval.end)
        #         # intervals[0].end = newInterval.end
        #         return intervals
        #     i, j = 0, 0
        #     while i < len_intervals-1 and j < len_intervals:
        #         if intervals[i].start <= newInterval.start and newInterval.start <= intervals[i].end:
        #             if newInterval.end <= intervals[i].end:
        #                 return intervals
        #             else:
        #                 j+=1
        #                 while j < len_intervals:
        #                     if j == len_intervals-1 and intervals[j].end <= newInterval.end:
        #                         intervals[i].end = newInterval.end
        #                         return intervals[:i+1]
        #                     elif newInterval.end < intervals[j].start:
        #                         intervals[i].end = newInterval.end
        #                         return intervals
        #                     elif newInterval.end >= intervals[j].start and newInterval.end <= intervals[j].end:
        #                         intervals[i].end = intervals[j].end
        #                         return intervals[:i+1] + intervals[j+1:]
        #                     else:
        #                         j += 1
        #         elif newInterval.start > intervals[i].end and newInterval.start < intervals[i+1].start:
        #             if newInterval.end < intervals[i+1].end:
        #                 intervals[i].start = newInterval.start
        #                 return intervals
        #             j+=1
        #             while j < len_intervals:
        #                 if intervals[j].end >= newInterval.end:
        #                     intervals[i+1].start = newInterval.start
        #                     intervals[i+1].end = intervals[j].end
        #                     return intervals[:i+2]
        #             return intervals[:i+1] + [newInterval] + intervals[i+1:]
        #         else:
        #             i+=1
        #     if i == len_intervals-1:
        #         if intervals[i].end >= newInterval.start:
        #             intervals[i].end = max(newInterval.end, intervals[i].end)
        #             return intervals
        #         else:
        #             return intervals + [newInterval]


# test cases:
# [[1,2],[3,5],[6,7],[8,10],[12,16]]\n[4,8]
# [[1,5]]\n[2,3]
# [[1,5]]\n[2,7]
# [[1,5]]\n[5,7]
# [[1,5],[6,8]]\n[0,9]
# [[0,2],[3,3],[6,11]]\n[9,15]
# [[0,2],[3,3],[6,11]]\n[14,15]
# [[0,5],[9,12]]\n[7,16]
        
