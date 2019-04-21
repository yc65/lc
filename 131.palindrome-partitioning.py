#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (39.87%)
# Total Accepted:    158.9K
# Total Submissions: 393.8K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        def is_palindrome(st):
            len_st = len(st)
            for i in range(len_st):
                if st[i] != st[len_st-1-i]:
                    return False
            return True

        def recur(prev_path, s):
            if not s:
                self.res.append(prev_path)
            else:
                len_s = len(s)
                for i in range(1, len_s+1):
                    if is_palindrome(s[:i]):
                        recur(prev_path+[s[:i]], s[i:])
        recur([], s)
        return self.res

        
