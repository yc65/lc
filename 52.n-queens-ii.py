#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (50.97%)
# Total Accepted:    94.2K
# Total Submissions: 184.8K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
# 
# 
# 
# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.
# 
# Example:
# 
# 
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown
# below.
# [
# [".Q..",  // Solution 1
# "...Q",
# "Q...",
# "..Q."],
# 
# ["..Q.",  // Solution 2
# "Q...",
# "...Q",
# ".Q.."]
# ]
# 
# 
#
class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["."]*n for i in range(n)]
        def is_ok(row, col):
            for i in range(col):
                if board[row][i] == "Q":
                    return False
            for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == "Q":
                    return False
            for i, j in zip(range(row, n, 1), range(col, -1, -1)):
                if board[i][j] == "Q":
                    return False
            return True
        
        res = []

        def backtracking(b, col):
            if col >= n:
                res.append([''.join(i) for i in b])
                return True
            ret = False
            for row in range(n):
                if is_ok(row, col):
                    b[row][col] = "Q"
                    if backtracking(b, col+1) == True:
                        ret = True
                    b[row][col] = "."
            return ret
        backtracking(board, 0)  
        return len(res) 

