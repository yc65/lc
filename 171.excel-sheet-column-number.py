#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#
class Solution:
    def titleToNumber(self, s: str) -> int:
        len_s = len(s)
        res = 0
        for idx, c in enumerate(s):
            res += (26 ** (len_s-idx-1)) * (ord(c) - ord("A")+1)
        return res

