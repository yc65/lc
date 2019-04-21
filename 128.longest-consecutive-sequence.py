#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (41.05%)
# Total Accepted:    200.4K
# Total Submissions: 484.8K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# Your algorithm should run in O(n) complexity.
# 
# Example:
# 
# 
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
#
class Solution:
    # hash
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for num in set_nums:
            if num-1 not in set_nums:
                curr_length = 1
                curr_num = num
                while curr_num+1 in set_nums:
                    curr_num+=1
                    curr_length+=1
                longest = max(longest, curr_length)
        return longest

