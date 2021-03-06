#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (39.55%)
# Total Accepted:    263.6K
# Total Submissions: 664.2K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
# 
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# Given an integer n where 1 ≤ n ≤ 30, generate the n^th term of the
# count-and-say sequence.
# 
# Note: Each term of the sequence of integers will be represented as a
# string.
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "1"
# 
# 
# Example 2:
# 
# 
# Input: 4
# Output: "1211"
# 
#
class Solution:
    # recursion
    def countAndSay(self, n: int) -> str:
        def rec(n):
            if n == 1:
                return '1'
            seq = rec(n-1)
            res = ''
            prev = ''
            count = 0
            len_seq = len(seq)
            n = len_seq-1
            if len_seq == 1:
                return "1"+seq
            while n >= 0:
                curr = seq[n]
                if curr == prev:
                    count += 1
                else:
                    if count:
                        res = str(count) + str(prev) + res
                    count = 1
                if n == 0:
                    res = str(count)+str(curr)+res
                prev = curr
                n-=1
            return res
        return rec(n)
        
