#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (26.63%)
# Total Accepted:    485K
# Total Submissions: 1.8M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution:
    # dp solution
    # time O(n^2), space O(n^2)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        cache = [[0 for x in range(n)] for y in range(n)]
        max_len = 1
        start = 0

        # if k == 1 or k == 2; k is the length of potential palindrom string
        
        for i in range(n):
            cache[i][i] = 1
            start = i
        for i in range(n-1):
            if s[i] == s[i+1]:
                cache[i][i+1] = 1
                max_len = 2
                start = i
        #if k > 2:
        k = 3
        while k < n+1:
            i = 0 # note: i should be inside the while loop!
            while i < n-k+1:
                j = i+k-1
                if s[i] == s[j] and cache[i+1][j-1] == 1:
                    cache[i][j] = 1
                    if k >= max_len:
                        max_len = k
                        start = i
                i+=1
            k+=1

        return s[start:start+max_len]

