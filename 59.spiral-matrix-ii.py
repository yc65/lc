#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (45.59%)
# Total Accepted:    129.8K
# Total Submissions: 284.4K
# Testcase Example:  '3'
#
# Given a positive integer n, generate a square matrix filled with elements
# from 1 to n^2 in spiral order.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
# 
# 
#
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        curr = 1
        res = [[0] * n for i in range(n)]
        row_b, col_b = 0, 0
        row_e, col_e = n-1, n-1
        while row_b <= row_e and col_b <= col_e:
            for i in range(col_b, col_e+1):
                res[row_b][i] = curr
                curr += 1
            for i in range(row_b+1, row_e+1):
                res[i][col_e] = curr
                curr += 1
            for i in range(col_e-1, col_b-1, -1):
                res[row_e][i] = curr
                curr += 1
            for i in range(row_e-1, row_b, -1):
                res[i][col_b] = curr
                curr += 1

            row_b += 1
            row_e -= 1
            col_b += 1
            col_e -= 1
        return res




