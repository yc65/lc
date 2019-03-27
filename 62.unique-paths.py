#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (46.67%)
# Total Accepted:    267.7K
# Total Submissions: 572.8K
# Testcase Example:  '3\n2'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# Above is a 7 x 3 grid. How many possible unique paths are there?
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# 
# 
# Example 2:
# 
# 
# Input: m = 7, n = 3
# Output: 28
# 
#
class Solution:
    # solution 1: dp
    # def uniquePaths(self, m: int, n: int) -> int:
    #     if m == 0 or n == 0:
    #         return 0
    #     cache = [[0]*m for i in range(n)]
    #     for i in range(m):
    #         cache[0][i] = 1
    #     for j in range(n):
    #         cache[j][0] = 1
    #     for i in range(1, n):
    #         for j in range(1, m):
    #             cache[i][j] = cache[i-1][j] + cache[i][j-1]
    #     return cache[-1][-1]

    # solution 2: space optimiazed # NOTE: cache is 1-D
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        cache = [1] * m
        for i in range(n-1):
            for j in range(1, m):
                cache[j] += cache[j-1]
        return cache[-1]

    # solution 3: maths - Todo
