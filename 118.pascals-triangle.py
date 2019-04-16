#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (45.32%)
# Total Accepted:    241.5K
# Total Submissions: 532.8K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        prev = []      
        for i in range(numRows):
            curr = prev + [None]
            for j in range(i+1):
                if j == 0 or j == i:
                    curr[j] = 1
                else:
                    curr[j] = prev[j-1]+prev[j]
            res.append(curr)
            prev = curr
        return res


