#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (26.84%)
# Total Accepted:    100.2K
# Total Submissions: 370.1K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return the minimum cuts needed for a palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
# cut.
# 
# 
#
class Solution:
    # dp
    def minCut(self, s: str) -> int:
        if not s: return -1
        len_s = len(s)
        is_palindrome = [[False for i in range(len_s)] for j in range(len_s)]
        cut_count = [float('inf') for i in range(len_s)]
        for i in range(len_s):
            is_palindrome[i][i] = True
        for l in range(2, len_s+1):
            for i in range(len_s-l+1):
                j = i+l-1
                if l == 2:
                    is_palindrome[i][j] = (s[i] == s[j])
                else:
                    is_palindrome[i][j] = ((s[i] == s[j]) and is_palindrome[i+1][j-1])
        for i in range(len_s):
            if is_palindrome[0][i]:
                cut_count[i]=0
            else:
                for j in range(i):
                    if is_palindrome[j+1][i]:
                        cut_count[i] = min(cut_count[i], cut_count[j]+1)
        return cut_count[-1]


