#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (40.19%)
# Total Accepted:    204.7K
# Total Submissions: 506.4K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note:
# 
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
# 
# 
#
class Solution:
    # backtracking
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtracking(temp,start, cands, target):
            for idx, c in enumerate(cands):
                # notice below how to avoid duplicates! need to use the "start"
                # notice idx is the index in cands, not in candidates
                if idx > 0 and cands[idx-1] == cands[idx]:
                    continue
                if c == target:
                    res.append(temp+[c])
                elif c < target:
                    backtracking(temp+[c],idx+1, cands[idx+1:], target-c)
        backtracking([],0, candidates, target)
        return res
