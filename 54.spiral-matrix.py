#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (29.80%)
# Total Accepted:    215.4K
# Total Submissions: 722.6K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return [] # don't forget empty input
        res = []
        a, b = len(matrix)-1, len(matrix[0])-1
        i, j = 0, 0
        while i <= a and j <= b:
            if a == i:
                for k in range(j, b+1):
                    res.append(matrix[a][k])
                break
            if j == b:
                for k in range(i, a+1):
                    res.append(matrix[k][j])
                break
            for k in range(j, b+1):
                res.append(matrix[i][k])
            for k in range(i+1, a+1):
                res.append(matrix[k][b])
            for k in range(b-1, j-1, -1):
                res.append(matrix[a][k])
            for k in range(a-1, i, -1):
                res.append(matrix[k][i])
            i+=1
            j+=1
            a-=1
            b-=1
        return res

