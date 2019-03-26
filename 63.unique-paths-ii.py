#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (33.24%)
# Total Accepted:    188.4K
# Total Submissions: 566.5K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
# 
# 
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# 
#
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # cache = [[0] * m for i in range(n)]
        n = len(obstacleGrid)
        if n == 0:
            return 0
        m = len(obstacleGrid[0])
        if m == 0:
            return 0
        x, y = 0, 1 # Note: y should be initialized as 1
        # if the obstacle is in the first row or in the first column
        
        hit = False 
        while x < m:
            if hit:
                obstacleGrid[0][x] = 0  
            elif obstacleGrid[0][x] == 0:
                obstacleGrid[0][x] = 1  
            else:
                obstacleGrid[0][x] = 0  
                hit = True
            x+= 1
        hit = False
        # NOTE: the dp is the same as obstacleGrid, so if the first row has been modified
        # the first column to be modified should take in to the previoius modification 
        # into account
        if obstacleGrid[0][0] == 0:
            hit = True
        while y < n:
            if hit:
                obstacleGrid[y][0] = 0
            elif obstacleGrid[y][0] == 0:
                obstacleGrid[y][0] = 1
            else:
                obstacleGrid[y][0] = 0
                hit = True
            y+= 1

        for i in range(1, n):
            for j in range(1,m):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]


# test cases:
# [[0,1,0,0], [0,0,0,0], [0,0,0,0]]
# [[0,0,0,0], [1,0,0,0],[0,0,0,0]]
# [[1,1]]
# [[1],[0]]
# [[0,1],[0,0]]
