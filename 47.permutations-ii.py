#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (39.19%)
# Total Accepted:    225.3K
# Total Submissions: 572.1K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        nums.sort()
        res = []
        def backtracking(candidates, path):
            if not candidates: res.append(path)
            for idx, cand in enumerate(candidates):
                if idx > 0 and candidates[idx]==candidates[idx-1]:
                    continue
                backtracking(candidates[:idx] + candidates[idx+1:],path+[cand])
        backtracking(nums, [])
        return res
