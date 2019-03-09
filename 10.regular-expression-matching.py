#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (24.98%)
# Total Accepted:    279.4K
# Total Submissions: 1.1M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*'.
# 
# 
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# 
# 
# The matching should cover the entire input string (not partial).
# 
# Note:
# 
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# . or *.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
# 
# 
# Example 3:
# 
# 
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
# Example 4:
# 
# 
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore
# it matches "aab".
# 
# 
# Example 5:
# 
# 
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
# 
# 
#

# note: (not mentioned in the description):
# if s is empty and p is not empty, return true; if s is not empty, p is empty return false
# if both s and p are empty, return true
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]

        cache[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1): # cache[*][len(p)+1] all False since if p is empty, it's false
                first_match = i<len(s) and p[j] in (s[i], '.') # dot could be considered as any letter
                if j+1 < len(p) and p[j+1] == '*':
                    # for pattern char before star
                    # the first scenario, p[j] and s[i] are not matched (i.e. first_match is false), but s[i:] p[j+2] are are matched
                    # like "aab"\n"c*a*b*""  -- no extra s included
                    # the second scenario, p[j] and s[i] are matched, and s[i+1:] and p[j:] are matched -- more s included
                    cache[i][j] = cache[i][j+2] or first_match and cache[i+1][j]
                else:
                    # for pattern char not before star
                    # first_match has to be true and s[i+1:] and p[j+1:] has to be true
                    cache[i][j] = first_match and cache[i+1][j+1]
        return cache[0][0]
