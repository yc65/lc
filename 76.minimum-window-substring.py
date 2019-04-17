#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (30.05%)
# Total Accepted:    219.7K
# Total Submissions: 728.7K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# Example:
# 
# 
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# 
# 
# Note:
# 
# 
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
# 
#
class Solution:
    # hashmap + two pointers
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ''
        len_s = len(s)
        m = dict.fromkeys(t, 0) # NOTE the way of initialize a dictionary
        proc_dct = dict.fromkeys(t, 0)
        for c in t:
            m[c] += 1
        # print(m)
        min_win =(0, 0, len_s + 1)
        required = len(m)
        formed = 0
        i = j = 0
        while j < len_s:
            if s[j] in m:
                proc_dct[s[j]] += 1
                if proc_dct[s[j]] == m[s[j]]:
                    formed+=1
            while i<=j and formed == required:
                if j-i+1 < min_win[-1]:
                    min_win = (i, j, j-i+1)
                if s[i] in proc_dct:
                    proc_dct[s[i]] -= 1
                    if proc_dct[s[i]] < m[s[i]]:
                        formed-=1
                i+=1
            j+=1
        if min_win[-1] == len_s+1:
            return ""
        else:
            return s[min_win[0]:min_win[1]+1]

