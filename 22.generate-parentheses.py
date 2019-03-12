#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (53.21%)
# Total Accepted:    306.1K
# Total Submissions: 573.7K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(ans, left, right):
            if len(ans) == 2*n:
                res.append(ans)
                return
            if left < n:
                backtracking(ans+'(', left+1, right)
            if right < left:
                backtracking(ans+')', left, right +1)
        backtracking('', 0, 0)
        return res

