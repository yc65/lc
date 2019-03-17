#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (22.37%)
# Total Accepted:    165.1K
# Total Submissions: 735.8K
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*'.
# 
# 
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# 
# 
# The matching should cover the entire input string (not partial).
# 
# Note:
# 
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# ? or *.
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
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not
# match 'b'.
# 
# 
# Example 4:
# 
# 
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*'
# matches the substring "dce".
# 
# 
# Example 5:
# 
# 
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false
# 
# 
#
class Solution:
    # dp, similar to 10. regular expression matching
    def isMatch(self, s: str, p: str) -> bool:
        len_s = len(s)
        len_p = len(p)
        cache = [[False]*(len_p+1) for i in range(len_s+1)]
        # if it's empty string and empty patter
        cache[0][0] = True
        for j in range(1, len_p+1):
            if p[j-1] != '*':
                break
            cache[0][j] = True
        # notice i, j are for indices of cache, i-1, j-1 are the indices of s and p
        for i in range(1, len_s+1):
            for j in range(1, len_p+1):
                if p[j-1] in [s[i-1], '?']:
                    cache[i][j] = cache[i-1][j-1]
                elif p[j-1] == '*':
                    # notice this!
                    cache[i][j] = cache[i-1][j-1] or cache[i-1][j] or cache[i][j-1]
                else:
                    cache[i][j] = False
        return cache[-1][-1]

