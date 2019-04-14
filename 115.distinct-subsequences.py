#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#
# https://leetcode.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (34.61%)
# Total Accepted:    103.4K
# Total Submissions: 297.6K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# Given a string S and a string T, count the number of distinct subsequences of
# S which equals T.
# 
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ACE" is a
# subsequence of "ABCDE" while "AEC" is not).
# 
# Example 1:
# 
# 
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
# 
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
# 
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# 
# 
# Example 2:
# 
# 
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
# 
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
# 
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
# ⁠ ^  ^^
# babgbag
# ⁠   ^^^
# 
# 
#
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s or  not t: return 0
        len_s, len_t = len(s), len(t)
        cache = [[0]*(len_t) for x in range(len_s)]
        for i in range(len_s):
            if t[0] == s[i]:
                cache[i][0] = 1 + (cache[i-1][0] if i > 0 else 0)
            else:
                cache[i][0] = cache[i-1][0] if i >0 else 0
        # print(cache)
        for i in range(1,len_s):
            for j in range(1,len_t):
                if s[i] == t[j]:
                    cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
                else:
                    cache[i][j] = cache[i-1][j]
        return cache[-1][-1]

