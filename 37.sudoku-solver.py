#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
# https://leetcode.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (35.63%)
# Total Accepted:    119.7K
# Total Submissions: 334.5K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# A sudoku solution must satisfy all of the following rules:
# 
# 
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3
# sub-boxes of the grid.
# 
# 
# Empty cells are indicated by the character '.'.
# 
# 
# A sudoku puzzle...
# 
# 
# ...and its solution numbers marked in red.
# 
# Note:
# 
# 
# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique
# solution.
# The given board size is always 9x9.
# 
# 
#
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def find_empty():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        return [i, j]
            return []
        def validate_row(r, num):
            for j in range(9):
                if num == board[r][j]:
                    return False
            return True
        def validate_col(c, num):
            for i in range(9):
                if num == board[i][c]:
                    return False
            return True
        def validate_matrix(r, c, num):
            matrix_id_r = r//3
            matrix_id_c = c//3
            for i in range(matrix_id_r*3, (matrix_id_r+1)*3):
                for j in range(matrix_id_c*3, (matrix_id_c+1)*3):
                    if num == board[i][j]:
                        return False
            return True
        def solver():
            candidate = find_empty()
            if not candidate:
                return True
            r = candidate[0]
            c = candidate[1]
            for n in "123456789":
                if validate_row(r, n) and validate_col(c, n) and validate_matrix(r, c, n):
                    board[r][c] = n
                    if solver():
                        return True
                    board[r][c] = '.'
            return False
        
        solver()

        

