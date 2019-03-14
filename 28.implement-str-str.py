#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (31.26%)
# Total Accepted:    390.4K
# Total Submissions: 1.2M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
# 
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
# Example 1:
# 
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# 
# 
# Clarification:
# 
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
# 
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
# 
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        haystack_len = len(haystack)
        needle_len = len(needle)
        n = 0
        while n < haystack_len-needle_len+1:
            m = 0
            matched = True
            while m < needle_len:
                if haystack[n+m] == needle[m]:
                    m+=1
                else:
                    matched = False
                    break
            if matched == True:
                return n
            n+=1
        return -1


