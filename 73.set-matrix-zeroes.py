#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (39.12%)
# Total Accepted:    196K
# Total Submissions: 500K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
# 
# Example 1:
# 
# 
# Input: 
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# Output: 
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
# 
# 
# Example 2:
# 
# 
# Input: 
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# Output: 
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
# 
# 
#
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # use the first row and the first column to mark if there's a zero in the 
        # corresponding row or column
        # NOTE: since such mark is done in-place, special attention should be paied to 
        # the first colum and the first row. 
        # e.g. if the first row has zero, the matrix[0][0] will be set to zero, consequently, 
        # everything in the first column will be set to zero as well. 
        # So a signal of whether the first column should be set to zero is needed
        m = len(matrix)
        col_zero = False
        if m != 0:
            n = len(matrix[0])
            if n != 0:
                for i in range(m):
                    if matrix[i][0] == 0:
                        col_zero = True
                    for j in range(1, n):
                        if matrix[i][j] == 0:
                            matrix[i][0] = 0
                            matrix[0][j] = 0
                for i in range(1, m):
                    for j in range(1, n):
                        if not matrix[i][0] or not matrix[0][j]:
                            matrix[i][j] = 0
                if not matrix[0][0]:
                    for j in range(1, n):
                        matrix[0][j] = 0
                if col_zero:
                    for i in range(m):
                        matrix[i][0] = 0
        

