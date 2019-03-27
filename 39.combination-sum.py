#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (46.75%)
# Total Accepted:    312.3K
# Total Submissions: 664.1K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
# 
# The same repeated number may be chosen from candidates unlimited number of
# times.
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
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
# 
#
class Solution:
    # backtracking
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(temp, canddts, target):
            for idx, i in enumerate(canddts):
                if i == target:
                    res.append(temp+[i])
                elif i < target:
                    # notice use canddts[idx:] to avoide duplicated results
                    backtrack(temp+[i],canddts[idx:],target-i)
        
        backtrack([],candidates, target)
        return res

# test cases
# [2,3,5]\n8
# []\n1
# [3,6,7,9,4,5,2,3,2,2]\n4

