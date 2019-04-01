#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (41.64%)
# Total Accepted:    193.7K
# Total Submissions: 463.8K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
# 
#
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        # NOTE: the input is not necessarily sorted
        nums.sort()
        res = []
        def backtracking(curr, candidates):
            res.append(curr)
            for idx, c in enumerate(candidates):
                if idx == 0 or (idx > 0 and candidates[idx-1] != c):
                    backtracking(curr + [c], candidates[idx+1:])
        backtracking([], nums)
        return res
