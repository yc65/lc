#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (38.20%)
# Total Accepted:    284.2K
# Total Submissions: 742.3K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        res = ''
        if len_a<len_b:
            a, b, len_a, len_b = b, a, len_b, len_a
        n = 0
        plus_one = 0
        while n < len_a:
            if n < len_b:
                temp = int(a[len_a-1-n]) + int(b[len_b-1-n]) + plus_one
            else:
                temp = int(a[len_a-1-n]) + plus_one

            if temp >= 2:
                plus_one = 1
                res = str(temp-2) + res
            else:
                plus_one = 0
                res = str(temp) + res                
            n += 1
        if plus_one:
            res = '1'+res
        return res


