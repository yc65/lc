#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (35.91%)
# Total Accepted:    527.5K
# Total Submissions: 1.5M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#
class Solution:
    # Note: think through all possible conditions of the stack:
    # it could be empty when you're indexing
    # it could be non-empty in the end
    def isValid(self, s: str) -> bool:
        stack = []
        m = {")":"(", "]":"[", "}":"{"}
        if s == "" :
            return True
        if s[0] in m:
            return False
        for symbol in s:
            if symbol in m:
                # Note don't forget the first condition; ALWAYS CHECK IF INDEX IS OK
                if stack and m[symbol] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(symbol)
        if stack: return False # Note if in the end the stack is not empty, return false
        return True

