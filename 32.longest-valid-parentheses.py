#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (24.93%)
# Total Accepted:    175.9K
# Total Submissions: 703.6K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# Example 1:
# 
# 
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# 
# 
# Example 2:
# 
# 
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
# 
# 
#
class Solution:
    # Solution 1: use of stack
    def longestValidParentheses(self, s: str) -> int:
        len_s = len(s)
        if len_s == 0: return 0
        # a stack that stores the indices of "(" 
        # or the indices of ')' if ')' could not be matched
        # stack[-1] serves as the starting point for calculating
        # substring length
        stack = [-1] # when (), we could calculate length of 1-(-1)=2
        largest = 0
        res = 0
        
        for i in range(len_s):
            if s[i] == "(":
                stack.append(i)
            else: # if the current char is ")"
                if len(stack)>1 and s[stack[-1]] == "(":
                        stack.pop()
                        res = i-stack[-1]
                        if res>largest:
                            largest = res   
                else:
                    stack.append(i)                  
  
        return largest
    # solution 2: dp


