#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (46.34%)
# Total Accepted:    190.8K
# Total Submissions: 410.3K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#
class Solution:
    # backtracking
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, curr):
            if len(curr) == k:
                # print (curr)
                res.append(curr)
                return
            for i in range(start, n+1):
                backtrack(i+1, curr+[i])
        backtrack(1, [])
        return res


