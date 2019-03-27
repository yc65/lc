#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (36.68%)
# Total Accepted:    162.7K
# Total Submissions: 442.3K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.
# 
# You have the following 3 operations permitted on a word:
# 
# 
# Insert a character
# Delete a character
# Replace a character
# 
# 
# Example 1:
# 
# 
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# 
# 
# Example 2:
# 
# 
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
# 
# 
#
class Solution:
    # dp
    def minDistance(self, word1: str, word2: str) -> int:
        len_word1 = len(word1)
        len_word2 = len(word2)
        cache = [[0] * (len_word2+1) for i in range(len_word1+1)]
        for i in range(len_word1+1):
            cache[i][0] = i
        for j in range(len_word2+1):
            cache[0][j] = j
        # print(cache)
        if len_word1==0 or len_word2 == 0:
            return cache[-1][-1]
        # NOTE: dp starts from 1
        for i in range(1, len_word1+1):
            for j in range(1, len_word2+1):
                if word1[i-1] == word2[j-1]:
                    cache[i][j] = cache[i-1][j-1]
                else:
                    cache[i][j] = 1 + min(cache[i-1][j], cache[i][j-1], cache[i-1][j-1])
        # print(cache)
        return cache[-1][-1]

