#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Hard (27.45%)
# Total Accepted:    107.4K
# Total Submissions: 389.1K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and
# s2.
# 
# Example 1:
# 
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# 
# 
#
class Solution:
    # dp
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1+len_s2 != len(s3):
            return False
        cache = [[None]*(len_s2+1) for i in range(len_s1+1)]
        cache[0][0] = True
        # print(cache)
        for j in range(1, len_s2+1):
            if s2[j-1] == s3[j-1] and cache[0][j-1]:
                cache[0][j] = True
            else:
                cache[0][j] = False
        
        for i in range(1, len_s1+1):
            if s1[i-1] == s3[i-1] and cache[i-1][0]:
                cache[i][0] = True
            else:
                cache[i][0] = False
        # print(cache)
        for i in range(1, len_s1+1):
            for j in range(1, len_s2+1):
                # print(cache[i-1])
                if (cache[i-1][j] and s1[i-1] == s3[i+j-1]) or (cache[i][j-1] and s2[j-1] == s3[i+j-1]):
                    cache[i][j] = True
                else:
                    cache[i][j] = False
        # print(cache)
        return cache[-1][-1]


