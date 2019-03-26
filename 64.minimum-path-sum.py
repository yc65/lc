#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (45.85%)
# Total Accepted:    215.7K
# Total Submissions: 469.5K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example:
# 
# 
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# 
#
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        if col == 0:
            return 0

        for i in range(1,row):
            grid[i][0] = grid[i][0] + grid[i-1][0]
        for j in range(1, col):
            grid[0][j] = grid[0][j] + grid[0][j-1]

        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] = grid[i][j] + min(grid[i][j-1], grid[i-1][j])
        return grid[-1][-1]

