#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.21%)
# Total Accepted:    634.4K
# Total Submissions: 2.5M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#
class Solution:
    def myAtoi(self, str: str) -> int:
        max_int = 2**31-1
        min_int = -2**31
        positive = True
        str_len = len(str)
        # char_to_digit = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6,"7":7, "8":8,"9":9, "0":0}
        idx = 0
        res = 0
        status = -1 # -1: unknown status; 1: appending digits

        while idx < str_len:
            c = str[idx]
            # temp = char_to_digit.get(c)
            temp = ord(c)-ord("0") # use this instead of dictionary to speedup
            if status == -1:
                if c == "-": 
                    positive = False
                    status = 1
                elif c == "+":
                    status = 1
                # elif temp != None:
                elif temp >=0 and temp<=9:
                    status = 1
                    res = res * 10 + temp
                elif c != " ":
                    return 0
            elif status == 1: 
                if temp >= 0 and temp<=9:
                    res = res*10+temp
                else:
                    break
            idx += 1
        if positive == True:
            if res > max_int:
                return max_int
            else:
                return res
        if positive == False:
            if 0-res < min_int:
                return min_int
            else:
                return 0-res
        

