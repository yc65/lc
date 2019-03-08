#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
# https://leetcode.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (14.50%)
# Total Accepted:    331.1K
# Total Submissions: 2.3M
# Testcase Example:  '"42"'
#
# Implement atoi which converts a string to an integer.
# 
# The function first discards as many whitespace characters as necessary until
# the first non-whitespace character is found. Then, starting from this
# character, takes an optional initial plus or minus sign followed by as many
# numerical digits as possible, and interprets them as a numerical value.
# 
# The string can contain additional characters after those that form the
# integral number, which are ignored and have no effect on the behavior of this
# function.
# 
# If the first sequence of non-whitespace characters in str is not a valid
# integral number, or if no such sequence exists because either str is empty or
# it contains only whitespace characters, no conversion is performed.
# 
# If no valid conversion could be performed, a zero value is returned.
# 
# Note:
# 
# 
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical
# value is out of the range of representable values, INT_MAX (2^31 − 1) or
# INT_MIN (−2^31) is returned.
# 
# 
# Example 1:
# 
# 
# Input: "42"
# Output: 42
# 
# 
# Example 2:
# 
# 
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus
# sign.
# Then take as many numerical digits as possible, which gets 42.
# 
# 
# Example 3:
# 
# 
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a
# numerical digit.
# 
# 
# Example 4:
# 
# 
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a
# numerical 
# digit or a +/- sign. Therefore no valid conversion could be performed.
# 
# Example 5:
# 
# 
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed
# integer.
# Thefore INT_MIN (−2^31) is returned.
# 
#


# test cases
# "-91283472332"
# "words and 987"
# "4193 with words"
# "   -42"
# "0000010"
# "   -000010"
# "  -0012a42"
# " b11228552307"

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

