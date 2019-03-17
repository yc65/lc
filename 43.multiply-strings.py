#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (29.97%)
# Total Accepted:    187K
# Total Submissions: 621.9K
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
# 
# Example 1:
# 
# 
# Input: num1 = "2", num2 = "3"
# Output: "6"
# 
# Example 2:
# 
# 
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# 
# 
# Note:
# 
# 
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len_num1 = len(num1)
        len_num2 = len(num2)
        res = [0]*(len_num1+len_num2)
        for j in range(len_num2-1, -1, -1):
            carry = 0 # note: unlike summation, carry could be 0-9
            for i in range(len_num1-1, -1, -1):
                temp = int(num2[j]) * int(num1[i]) + res[i+j+1] + carry
                if temp > 9:
                    res[i+j+1] = temp%10
                    carry = temp//10
                else:
                    carry = 0
                    res[i+j+1] = temp
            res[j] += carry
        res_str = ''.join(map(str, res))
        res_str = res_str.lstrip('0')
        if not res_str: res_str = "0"
        return res_str

