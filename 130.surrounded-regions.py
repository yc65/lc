#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (22.25%)
# Total Accepted:    140K
# Total Submissions: 621.8K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# Example:
# 
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# After running your function, the board should be:
# 
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# Explanation:
# 
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
#
class Solution:
    # dfs
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # the "O" on the boarder and it's children should remains to be "O"
        # Other "O" should be converted to "X"
        len_row = len(board)
        if len_row:
            len_col = len(board[0])
            if len_col:
                def dfs(x, y):
                    if board[x][y] == "C":
                        board[x][y] = "O"
                        if x> 0:
                            dfs(x-1, y)
                        if x<len_row-1:
                            dfs(x+1, y)
                        if y > 0:
                            dfs(x, y-1)
                        if y <len_col-1:
                            dfs(x, y+1)
                for i in range(len_row):
                    for j in range(len_col):
                        if board[i][j] == 'O':
                            board[i][j] = "C"
                for i in range(len_row):
                    if board[i][0] == "C":
                        dfs(i, 0)
                    if board[i][len_col-1] == "C":
                        dfs(i, len_col-1)
                for j in range(len_col):
                    if board[0][j] == "C":
                        dfs(0, j)
                    if board[len_row-1][j] == "C":
                        dfs(len_row-1, j)
                for i in range(len_row):
                    for j in range(len_col):
                        if board[i][j] == "C":
                            board[i][j] = "X"

