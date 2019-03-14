#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (16.08%)
# Total Accepted:    182.5K
# Total Submissions: 1.1M
# Testcase Example:  '10\n3'
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division and mod operator.
# 
# Return the quotient after dividing dividend by divisor.
# 
# The integer division should truncate toward zero.
# 
# Example 1:
# 
# 
# Input: dividend = 10, divisor = 3
# Output: 3
# 
# Example 2:
# 
# 
# Input: dividend = 7, divisor = -3
# Output: -2
# 
# Note:
# 
# 
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 2^31 − 1 when the division
# result overflows.
# 
# 
#
class Solution:
    # bit operation:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend>0) ^ (divisor>0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        count = 1
        temp = divisor
        while dividend >= divisor:
            while dividend >= temp:
                temp <<= 1
                count <<=1
            count >>= 1
            # print("count ", count)
            res += count
            temp >>=1
            # print ("temp ",temp)
            dividend -= temp
            temp = divisor
            count = 1
        if negative:
            res = 0-res
        return min(max(res, -2**31), 2**31-1)

