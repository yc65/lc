#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (26.72%)
# Total Accepted:    767K
# Total Submissions: 2.9M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# '"tmmzuxt"'
# 
# 
# 
#
class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        sub_begin = 0
        sub_end = -1
        res = 0
        cache = {} # store the most recent index of the char in the str
        n = 0
        # loop through the string
        for c in s:
            temp = cache.get(c)
            # if the char is in the substring
            if temp != None and temp>=sub_begin:
                    sub_begin  = temp+1
                    cache[c] = n
                    sub_end =n
            else:
                cache[c] = n
                sub_end=n
            if sub_end-sub_begin +1> res:
                res = sub_end-sub_begin +1
            n += 1
        return res
        
