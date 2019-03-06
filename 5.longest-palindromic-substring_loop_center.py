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
    # centre around one point solution
    # time O(n^2), space O(1)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 1
        start = 0
        
        for i in range(1, n):
            # assume the substring has odd length
            low = i-1
            high = i+1
            while low >=0 and high<n and s[low] == s[high]:
                if high - low + 1 >= max_len:
                    max_len = high-low+1
                    start = low
                high+=1
                low -= 1
            # assue the substring has even length
            low = i-1
            high = i
            while low >=0 and high<n and s[low] == s[high]:
                if high-low +1>= max_len:
                    max_len = high-low+1
                    start = low
                high+=1
                low-=1
        return s[start:start+max_len]                  

