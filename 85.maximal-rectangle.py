#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
# https://leetcode.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (32.58%)
# Total Accepted:    114.8K
# Total Submissions: 351.3K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# Output: 6
# 
# 
#
class Solution:
    # dp. 
    # 优先考虑height。 在高度最大的情况下，计算可以容许的最大宽度，进而得到最大面积
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        max_area = 0
        height = [0]*n
        left = [0]*n # left, right [l, r)
        right = [n]*n
        for i in range(m):
            curr_left, curr_right = 0, n
            # calculate the maximum height of the item so far
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], curr_left)
                else: # there's no left boundary, we just set it to zero
                      # when mutiplied with the height[i][j], which is zero, the area is zero
                    left[j] = 0
                    curr_left = j+1
            for j in range(n-1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], curr_right)
                else: # there's no right boundary, we just set it to n
                      # when mutiplied with the height[i][j], which is zero, the area is zero
                    right[j] = n
                    curr_right = j
            # print(height, left, right)
            for j in range(n):
                max_area = max(max_area, height[j] * (right[j]-left[j]))
        
        return max_area

