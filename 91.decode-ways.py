#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (21.98%)
# Total Accepted:    246.1K
# Total Submissions: 1.1M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
# 
# Example 1:
# 
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# Example 2:
# 
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
# 
#
class Solution:
    # DP
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        len_s = len(s)
        cache = [1]*(len(s)+1)
        cache[1] = 1
        idx = 1
        # NOTE: special treatment of zero
        # if the char preceding zero is larger than 2: return 0
        # if char preceding zero is 1 or 2: cache[idx] == cache[idx-2]
        # if it's single zero, return 0
        while idx < len_s:
            if s[idx] == '0' and (s[idx-1]!='1' and s[idx-1]!='2'): return 0
            if int(s[idx-1:idx+1])<=26 and int(s[idx-1:idx+1])>=10:
                if s[idx] == '0':
                    cache[idx+1] = cache[idx-1]
                else:
                    cache[idx+1] = cache[idx-1]+cache[idx]
            else:
                cache[idx+1] = cache[idx]
            idx += 1
        return cache[-1]

