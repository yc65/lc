#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image/description/
#
# algorithms
# Medium (46.86%)
# Total Accepted:    230.5K
# Total Submissions: 489.1K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# You are given an n x n 2D matrix representing an image.
# 
# Rotate the image by 90 degrees (clockwise).
# 
# Note:
# 
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
# 
# Example 1:
# 
# 
# Given input matrix = 
# [
# ⁠ [1,2,3],
# ⁠ [4,5,6],
# ⁠ [7,8,9]
# ],
# 
# rotate the input matrix in-place such that it becomes:
# [
# ⁠ [7,4,1],
# ⁠ [8,5,2],
# ⁠ [9,6,3]
# ]
# 
# 
# Example 2:
# 
# 
# Given input matrix =
# [
# ⁠ [ 5, 1, 9,11],
# ⁠ [ 2, 4, 8,10],
# ⁠ [13, 3, 6, 7],
# ⁠ [15,14,12,16]
# ], 
# 
# rotate the input matrix in-place such that it becomes:
# [
# ⁠ [15,13, 2, 5],
# ⁠ [14, 3, 4, 1],
# ⁠ [12, 6, 8, 9],
# ⁠ [16, 7,10,11]
# ]
# 
# 
#
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # my solution
        n = len(matrix)
        count = 0
        max_idx = n-1
        if n%2 == 0:
            mid = n//2-1
        else:
            mid = n//2
        while count <= mid:
            # print("count: ",count)
            for i in range(count, max_idx-count):
                # print("i: ", i)
                matrix[i][count], matrix[count][max_idx-i] = matrix[count][max_idx-i],matrix[i][count]
                # print("1: ", matrix)
                matrix[i][count], matrix[max_idx-i][max_idx-count] = matrix[max_idx-i][max_idx-count],matrix[i][count]
                # print("2: ", matrix)
                matrix[i][count], matrix[max_idx-count][i] = matrix[max_idx-count][i],matrix[i][count]
                # print("3: ", matrix)
            count += 1

        # (from discussion) modify in-place: two symmetrically transformations,firstly along diagonal,then along central axis
        # n=len(matrix)
        # for i in range(n):
        #     for j in range(i,n):
        #         matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        # for i in range(n):
        #     for j in range(int(n/2)):
        #         matrix[i][j],matrix[i][n-1-j]=matrix[i][n-1-j],matrix[i][j]
        
        # runtime are the same
