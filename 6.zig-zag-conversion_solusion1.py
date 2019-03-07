#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (30.72%)
# Total Accepted:    289.6K
# Total Submissions: 942.3K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
#
class Solution:
    # solution 1: loop through the s; sort by row
    def convert(self, s: str, numRows: int) -> str:
        res = ["" for i in range(numRows)] # notice: [[]*3] doesn't work!
                                           # notice: use string instead of list to speed up
        res_count = 0
        direction = 0 # 0 for down, 1 for up
        n = 0 # record which row currently we are in
        len_s = len(s) # notice: calculate len_s upfront to speed up

        if numRows == 1: return s # notice! for testcase "ABC"\n1

        while n < numRows: 
            if res_count == len_s:
                return  "".join(res)
            if direction == 0:
                res[n]+=s[res_count]
                res_count += 1
                if n == numRows-1:
                    direction = 1
                    n -= 1
                else:
                    n += 1
            elif direction == 1:
                res[n]+=s[res_count]
                res_count+=1
                if n == 0:
                    direction = 0
                    n += 1
                else:
                    n -= 1

# ✔ Accepted
#   ✔ 1158/1158 cases passed (92 ms)
#   ✔ Your runtime beats 63.07 % of python3 submissions
#   ✔ Your memory usage beats 10.59 % of python3 submissions (13.3 MB)
