#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (51.41%)
# Total Accepted:    342.1K
# Total Submissions: 663K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
class Solution:
    # backtracking:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # len_nums = len(nums)
        res = []
        def backtracking(candidites, curr):
            # print(candidites, curr)
            res.append(curr)
            if candidites:
                for idx, item in enumerate(candidites):
                    # print (candidites, curr, item)
                    # NOTE the start for the candidates for the next loop is idx+1, not 1
                    backtracking(candidites[idx+1:], curr+[item])

        backtracking(nums, [])
        return res

